#!/usr/bin/env python3
"""
One-shot normalization tool for C++ templates/solutions.

Usage:
  # Dry run (no files modified)
  python3 tools/normalize_cpp_namespace.py

  # Apply changes (will create .bak backups)
  python3 tools/normalize_cpp_namespace.py --apply

This script is intentionally conservative: it finds `template.cpp` and `solution.cpp`
files, inserts `using namespace std;` after the last include (if missing), and removes
`std::` prefixes from code (avoiding changes inside string literals and comments).

Run this only when you are ready to validate changes with Judge0/orchestrator.
"""
from pathlib import Path
import re
import argparse
import difflib
import sys


CPP_TARGET_NAMES = {"template.cpp", "solution.cpp"}


def mask_strings_and_comments(src: str):
    # Mask block comments, line comments and string literals so replacements don't touch them.
    masks = []

    def _mask(pattern, text, flags=0):
        nonlocal masks
        out = []
        last = 0
        for m in re.finditer(pattern, text, flags):
            out.append(text[last:m.start()])
            placeholder = f"__MASK_{len(masks)}__"
            masks.append(m.group(0))
            out.append(placeholder)
            last = m.end()
        out.append(text[last:])
        return ''.join(out)

    # 1) Mask block comments /* ... */
    t = _mask(r'/\*.*?\*/', src, flags=re.S)
    # 2) Mask double-quoted strings
    t = _mask(r'"(?:\\.|[^"\\])*"', t)
    # 3) Mask single-quoted chars
    t = _mask(r"'(?:\\.|[^'\\])'", t)
    # 4) Mask line comments //...
    t = _mask(r'//.*?$', t, flags=re.M)

    return t, masks


def unmask(text: str, masks):
    for i, original in enumerate(masks):
        text = text.replace(f"__MASK_{i}__", original)
    return text


def add_using_namespace(src: str):
    if 'using namespace std;' in src:
        return src, False

    includes = list(re.finditer(r'^\s*#\s*include\b.*$', src, flags=re.M))
    if not includes:
        # No includes; don't add using namespace std; to avoid polluting global files.
        return src, False

    last = includes[-1]
    insert_pos = last.end()
    before = src[:insert_pos]
    after = src[insert_pos:]
    new_src = before + "\nusing namespace std;\n" + after
    return new_src, True


def strip_std_prefixes(src: str):
    masked, masks = mask_strings_and_comments(src)
    # Avoid replacing inside include lines
    lines = masked.splitlines(True)
    for i, line in enumerate(lines):
        if line.lstrip().startswith('#include'):
            # keep include line as-is
            continue
        lines[i] = line.replace('std::', '')
    replaced = ''.join(lines)
    return unmask(replaced, masks)


def process_file(path: Path, apply: bool):
    src = path.read_text(encoding='utf-8')
    new_src = src
    changed = False

    # Ensure using namespace std; after includes
    new_src, added_using = add_using_namespace(new_src)

    # Remove std:: prefixes conservatively
    new_src2 = strip_std_prefixes(new_src)
    if new_src2 != new_src:
        new_src = new_src2
        changed = True

    # If we only added using namespace std; that counts as change
    if added_using:
        changed = True

    if not changed:
        return False, None

    diff = ''.join(difflib.unified_diff(
        src.splitlines(keepends=True),
        new_src.splitlines(keepends=True),
        fromfile=str(path),
        tofile=str(path) + '.normalized'
    ))

    if apply:
        backup = path.with_suffix(path.suffix + '.bak')
        path.rename(backup)
        path.write_text(new_src, encoding='utf-8')
        return True, diff
    else:
        return True, diff


def find_targets(root: Path):
    targets = []
    for p in root.rglob('*.cpp'):
        if p.name in CPP_TARGET_NAMES:
            # skip wrappers explicitly
            if 'wrapper.cpp' in p.name:
                continue
            targets.append(p)
    return targets


def main():
    ap = argparse.ArgumentParser(description='Normalize C++ namespace usage in templates/solutions (dry-run by default)')
    ap.add_argument('--apply', action='store_true', help='Write changes to disk (creates .bak backups)')
    ap.add_argument('--root', default='.', help='Repository root')
    args = ap.parse_args()

    root = Path(args.root).resolve()
    targets = find_targets(root)
    if not targets:
        print('No target files found.')
        return 0

    any_changes = False
    for f in targets:
        changed, diff = process_file(f, apply=args.apply)
        if changed:
            any_changes = True
            print(f'--- {f} would be changed ---' if not args.apply else f'*** {f} changed (backup created) ***')
            if diff:
                print(diff)

    if not any_changes:
        print('No changes needed.')
    else:
        if not args.apply:
            print('\nDRY RUN complete. To apply changes, re-run with --apply. Backups will be made as .bak files.')
        else:
            print('\nChanges applied. Run your CI/tests (or orchestrator) to validate.')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
