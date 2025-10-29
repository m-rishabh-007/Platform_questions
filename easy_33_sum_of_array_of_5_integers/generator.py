import random
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    if rule_type == "edge_cases":
        cases = [
            [0, 0, 0, 0, 0],
            [100, 100, 100, 100, 100],
            [-100, -100, -100, -100, -100],
            [1, -1, 1, -1, 0],
            [2147483647, 0, 0, 0, -2147483648]
        ]
        arr = rng.choice(cases)
        return " ".join(map(str, arr)) + "\n"
    if rule_type == "small":
        arr = [rng.randint(-10, 10) for _ in range(5)]
        return " ".join(map(str, arr)) + "\n"
    if rule_type == "medium":
        arr = [rng.randint(-1000, 1000) for _ in range(5)]
        return " ".join(map(str, arr)) + "\n"
    if rule_type == "large":
        arr = [rng.randint(-1000000, 1000000) for _ in range(5)]
        return " ".join(map(str, arr)) + "\n"
    raise ValueError(f"Unhandled rule_type: {rule_type}")

if __name__ == "__main__":
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("rule_type")
    parser.add_argument("--args", type=json.loads, default="{}")
    parser.add_argument("--rng-seed", type=int, default=None)
    ns = parser.parse_args()
    if ns.rng_seed is not None:
        ns.args["seed"] = ns.rng_seed
    print(generate_case(ns.rule_type, ns.args), end="")
