import random
import json
import sys

def generate_case(rule_type, args):
    """Generate a single test case based on rule_type and args.
    
    This function is called by orchestrator.py with command-line args:
    - rule_type: one of "edge_cases", "small", "medium", "large", "stress"
    - args: dict with optional parameters (may include "seed" for RNG)
    
    Returns a string representing the INPUT only (no expected output).
    The string should end with \n and match the format expected by wrapper.py.
    """
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        # TODO: Define edge cases for this problem
        # Examples: empty input, single element, boundary values, special cases
        edge_cases = [
            "0\n",
            "1\n",
        ]
        return rng.choice(edge_cases)
    
    elif rule_type == "small":
        # TODO: Generate small test cases (quick to run)
        value = rng.randint(1, 10)
        return f"{value}\n"
    
    elif rule_type == "medium":
        # TODO: Generate medium-sized test cases
        value = rng.randint(10, 100)
        return f"{value}\n"
    
    elif rule_type == "large":
        # TODO: Generate large test cases
        value = rng.randint(100, 1000)
        return f"{value}\n"
    
    elif rule_type == "stress":
        # TODO: Generate stress test cases (maximum constraints)
        value = rng.randint(1000, 10000)
        return f"{value}\n"
    
    raise ValueError(f"Unhandled rule_type: {rule_type}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("rule_type")
    parser.add_argument("--args", type=json.loads, default="{}")
    parser.add_argument("--rng-seed", type=int, default=None)
    ns = parser.parse_args()
    if ns.rng_seed is not None:
        ns.args["seed"] = ns.rng_seed
    print(generate_case(ns.rule_type, ns.args), end="")
