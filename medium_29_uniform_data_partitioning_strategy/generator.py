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
        # Edge cases for data partitioning
        edge_cases = [
            [12],           # Single volume
            [17, 23],       # Coprime numbers
            [50, 50, 50],   # Identical volumes
            [6, 12, 18],    # Common factors
            [24, 36, 60],   # Example from description
        ]
        
        volumes = rng.choice(edge_cases)
        n = len(volumes)
        return f"{n}\n{' '.join(map(str, volumes))}\n"

    if rule_type == "small":
        # Small test cases (2-5 volumes)
        n = rng.randint(2, 5)
        volumes = [rng.randint(1, 100) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, volumes))}\n"
    
    if rule_type == "medium":
        # Medium test cases (6-20 volumes)
        n = rng.randint(6, 20)
        volumes = [rng.randint(1, 1000) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, volumes))}\n"
    
    if rule_type == "large":
        # Large test cases (21-100 volumes)
        n = rng.randint(21, 100)
        volumes = [rng.randint(1, 10000) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, volumes))}\n"
    
    if rule_type == "extra_large":
        # Extra large test cases (101-1000 volumes)
        n = rng.randint(101, 1000)
        volumes = [rng.randint(1, 1000000) for _ in range(n)]
        return f"{n}\n{' '.join(map(str, volumes))}\n"

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