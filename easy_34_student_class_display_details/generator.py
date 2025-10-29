import random
import sys
import string

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    def rand_name():
        return ''.join(rng.choices(string.ascii_letters, k=rng.randint(3, 8)))
    if rule_type == "edge_cases":
        cases = [
            ("A", 0, 0.0),
            ("Z", 99999, -100.5),
            ("Test", 1, 100.0),
            ("Bob", 202, 0.0),
            ("Alice", 101, 89.5)
        ]
        name, roll, marks = rng.choice(cases)
        return f"{name} {roll} {marks}\n"
    if rule_type == "small":
        name = rand_name()
        roll = rng.randint(1, 10)
        marks = round(rng.uniform(0, 100), 1)
        return f"{name} {roll} {marks}\n"
    if rule_type == "medium":
        name = rand_name()
        roll = rng.randint(10, 1000)
        marks = round(rng.uniform(-100, 100), 2)
        return f"{name} {roll} {marks}\n"
    if rule_type == "large":
        name = rand_name()
        roll = rng.randint(1000, 99999)
        marks = round(rng.uniform(-1000, 1000), 3)
        return f"{name} {roll} {marks}\n"
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
