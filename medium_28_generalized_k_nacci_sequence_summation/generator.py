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
        # Edge cases for k-nacci sequence
        edge_cases = [
            (0, 2),     # Minimal case
            (1, 2),     # Base case
            (2, 3),     # All base cases for tribonacci
            (3, 3),     # First computed term for tribonacci
            (5, 2),     # Classic Fibonacci
            (10, 5),    # Larger k
        ]
        
        n, k = rng.choice(edge_cases)
        return f"{n}\n{k}\n"

    if rule_type == "small":
        # Small test cases
        n = rng.randint(0, 20)
        k = rng.randint(2, 5)
        return f"{n}\n{k}\n"
    
    if rule_type == "medium":
        # Medium test cases
        n = rng.randint(21, 100)
        k = rng.randint(2, 10)
        return f"{n}\n{k}\n"
    
    if rule_type == "large":
        # Large test cases
        n = rng.randint(101, 500)
        k = rng.randint(2, 20)
        return f"{n}\n{k}\n"
    
    if rule_type == "extra_large":
        # Extra large test cases
        n = rng.randint(501, 1000)
        k = rng.randint(2, 50)
        return f"{n}\n{k}\n"

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