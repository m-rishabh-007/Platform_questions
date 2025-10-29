import random
import json
import sys

def generate_matrix(m, n, min_val, max_val, rng):
    """Generate a random m x n matrix"""
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(rng.randint(min_val, max_val))
        matrix.append(row)
    return matrix

def format_input(m, n, matrix):
    """Format matrix as input string"""
    lines = [f"{m} {n}"]
    for row in matrix:
        lines.append(' '.join(map(str, row)))
    return '\n'.join(lines)

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            (1, 1),
            (1, rng.randint(2, 10)),
            (rng.randint(2, 10), 1),
            (2, 2),
            (3, 3)
        ]
        m, n = rng.choice(edge_types)
        matrix = generate_matrix(m, n, -1000, 1000, rng)
        return format_input(m, n, matrix) + "\n"
    
    elif rule_type == "small":
        m = rng.randint(2, 5)
        n = rng.randint(2, 5)
        matrix = generate_matrix(m, n, -1000, 1000, rng)
        return format_input(m, n, matrix) + "\n"
    
    elif rule_type == "medium":
        m = rng.randint(5, 20)
        n = rng.randint(5, 20)
        matrix = generate_matrix(m, n, -1000, 1000, rng)
        return format_input(m, n, matrix) + "\n"
    
    elif rule_type == "large":
        m = rng.randint(20, 100)
        n = rng.randint(20, 100)
        matrix = generate_matrix(m, n, -1000, 1000, rng)
        return format_input(m, n, matrix) + "\n"
    
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
