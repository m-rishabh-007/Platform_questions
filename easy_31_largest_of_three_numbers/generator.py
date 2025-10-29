import random
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    if rule_type == "edge_cases":
        cases = [
            (0, 0, 0),
            (-100, -100, -100),
            (100, 100, 100),
            (0, -1, 1),
            (2147483647, -2147483648, 0)
        ]
        a, b, c = rng.choice(cases)
        return f"{a} {b} {c}\n"
    if rule_type == "small":
        a = rng.randint(-10, 10)
        b = rng.randint(-10, 10)
        c = rng.randint(-10, 10)
        return f"{a} {b} {c}\n"
    if rule_type == "medium":
        a = rng.randint(-1000, 1000)
        b = rng.randint(-1000, 1000)
        c = rng.randint(-1000, 1000)
        return f"{a} {b} {c}\n"
    if rule_type == "large":
        a = rng.randint(-1000000, 1000000)
        b = rng.randint(-1000000, 1000000)
        c = rng.randint(-1000000, 1000000)
        return f"{a} {b} {c}\n"
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
