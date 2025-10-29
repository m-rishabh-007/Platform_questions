"""Problem-specific test case generator.

This script is called by `orchestrator.py` with JSON arguments that match
the `generation_logic` section of `config.json`. Implement the
`generate_case` function so that it produces _exactly one_ test case using
the provided rule arguments and prints it to STDOUT in the format expected
by the wrappers.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from typing import Any, Dict


def generate_case(rule_type: str, args: Dict[str, Any]) -> str:
    """Return the stdin payload for a single test case.

    Parameters
    ----------
    rule_type: str
        One of the keys defined in `config.json` (for example,
        \"edge_cases\", \"small\", \"large\"). Use this to select
        between different generation strategies.
    args: Dict[str, Any]
        JSON-compatible data that describes how to build the test case.

    Returns
    -------
    str
        A newline-terminated string that will be written directly to STDOUT.
    """

    rng = random.Random(args.get("seed"))

    if rule_type == "edge_cases":
        # Edge cases for sorting analysis
        edge_cases = [
            [1],  # Single element
            [1, 2],  # Already sorted
            [2, 1],  # Reverse sorted
            [1, 1, 1],  # All same elements
            [3, 1, 2],  # Minimal unsorted
            [5, 4, 3, 2, 1],  # Fully reverse
        ]
        
        case = rng.choice(edge_cases)
        n = len(case)
        return f"{n}\n{' '.join(map(str, case))}\n"

    if rule_type == "small":
        # Small arrays (2-10 elements)
        n = rng.randint(2, 10)
        arr = [rng.randint(-50, 50) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, arr))}\n"
    
    if rule_type == "medium":
        # Medium arrays (11-100 elements)
        n = rng.randint(11, 100)
        arr = [rng.randint(-500, 500) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, arr))}\n"
    
    if rule_type == "large":
        # Large arrays (101-500 elements)
        n = rng.randint(101, 500)
        arr = [rng.randint(-1000, 1000) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, arr))}\n"
    
    if rule_type == "extra_large":
        # Extra large arrays (501-1000 elements)
        n = rng.randint(501, 1000)
        arr = [rng.randint(-1000, 1000) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, arr))}\n"

    raise ValueError(f"Unhandled rule_type: {rule_type}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Problem generator stub")
    parser.add_argument("rule_type", help="Name of the bucket being generated")
    parser.add_argument(
        "--args",
        type=json.loads,
        default="{}",
        help="JSON blob with configuration for this rule",
    )
    parser.add_argument(
        "--rng-seed",
        type=int,
        default=None,
        help="Optional seed override for deterministic debugging",
    )
    parsed = parser.parse_args(argv)
    if parsed.rng_seed is not None:
        parsed.args["seed"] = parsed.rng_seed
    return parsed


def main(argv: list[str]) -> int:
    namespace = parse_args(argv)

    try:
        payload = generate_case(namespace.rule_type, namespace.args)
    except Exception as exc:  # noqa: BLE001
        print(f"Generator error: {exc}", file=sys.stderr)
        return 1

    sys.stdout.write(payload)
    if not payload.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))