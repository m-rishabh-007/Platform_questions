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
        # Edge cases for Emirp generation
        edge_cases = [
            1,      # No Emirps
            10,     # No Emirps (only single digit primes and palindromic 11)
            12,     # Still no Emirps
            13,     # First Emirp
            20,     # Small range with 2 Emirps
            50,     # Medium range
        ]
        
        case = rng.choice(edge_cases)
        return f"{case}\n"

    if rule_type == "small":
        # Small limits (10-200)
        limit = rng.randint(10, 200)
        return f"{limit}\n"
    
    if rule_type == "medium":
        # Medium limits (201-1000)
        limit = rng.randint(201, 1000)
        return f"{limit}\n"
    
    if rule_type == "large":
        # Large limits (1001-5000)
        limit = rng.randint(1001, 5000)
        return f"{limit}\n"
    
    if rule_type == "extra_large":
        # Extra large limits (5001-10000)
        limit = rng.randint(5001, 10000)
        return f"{limit}\n"

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