import random
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    if rule_type == "edge_cases":
        cases = [0, 1, 20]
        n = rng.choice(cases)
        return f"{n}\n"
    if rule_type == "small":
        n = rng.randint(0, 5)
        return f"{n}\n"
    if rule_type == "medium":
        n = rng.randint(6, 15)
        return f"{n}\n"
    if rule_type == "large":
        n = rng.randint(16, 20)
        return f"{n}\n"
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
