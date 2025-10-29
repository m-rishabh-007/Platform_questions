# Tools Directory

This directory contains utility scripts for maintaining and migrating the codebase.

## normalize_cpp_namespace.py

**Purpose:** One-time batch normalization of C++ files to match platform standards.

**Use Case:** Migrate legacy problems (e.g., `easy_21` through `easy_35`) to use the standard namespace format:
- Adds `using namespace std;` after includes (if missing)
- Removes `std::` prefixes from code
- Skips `wrapper.cpp` files (intentionally)
- Creates `.bak` backups before any changes

**When to Use:**
- ✅ Migrating old problems to match 30_oct/ standards
- ✅ Batch cleanup of existing problems with inconsistent namespace usage
- ❌ NOT for new problem creation (use 30_oct/ templates instead)
- ❌ NOT needed if problem already follows 30_oct/ format

**Usage:**

```bash
# Dry run (preview changes without modifying files)
python3 tools/normalize_cpp_namespace.py

# Apply changes (creates .bak backups)
python3 tools/normalize_cpp_namespace.py --apply

# Target specific directory
python3 tools/normalize_cpp_namespace.py --root easy_21_remove_duplicates_from_a_list/
```

**Important Notes:**
1. **Always dry-run first** to preview changes
2. **Validate with orchestrator** after applying changes
3. **New problems should use 30_oct/ templates** - they already have correct format
4. This tool is conservative: preserves strings, comments, and include directives

**See Also:**
- `.github/NORMALIZATION_LATER.md` - Detailed normalization workflow
- `templates/PLATFORM_CONTEXT.md` - Platform standards and architecture
- `30_oct/` - Canonical problem examples with correct format
