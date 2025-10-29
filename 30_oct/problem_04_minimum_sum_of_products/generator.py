import random
import json
import sys

def generate_arrays(len_A, len_B, min_val, max_val, rng):
    """Generate random arrays A and B"""
    A = [rng.randint(min_val, max_val) for _ in range(len_A)]
    B = [rng.randint(min_val, max_val) for _ in range(len_B)]
    return A, B

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            (5, 5),  # Equal lengths
            (10, 1),  # B size 1
            (3, 3),  # Small equal
            (7, 3),  # Normal case
        ]
        len_A, len_B = rng.choice(edge_types)
        
        # Special handling for all positive or all negative
        choice = rng.randint(0, 3)
        if choice == 2:  # All positive
            A, B = generate_arrays(len_A, len_B, 1, 1000, rng)
        elif choice == 3:  # All negative
            A, B = generate_arrays(len_A, len_B, -1000, -1, rng)
        else:
            A, B = generate_arrays(len_A, len_B, -1000, 1000, rng)
        
        return ' '.join(map(str, A)) + '\n' + ' '.join(map(str, B)) + '\n'
    
    elif rule_type == "small":
        len_A = rng.randint(2, 10)
        len_B = rng.randint(1, len_A)
        A, B = generate_arrays(len_A, len_B, -1000, 1000, rng)
        return ' '.join(map(str, A)) + '\n' + ' '.join(map(str, B)) + '\n'
    
    elif rule_type == "medium":
        len_A = rng.randint(10, 100)
        len_B = rng.randint(1, len_A)
        A, B = generate_arrays(len_A, len_B, -1000, 1000, rng)
        return ' '.join(map(str, A)) + '\n' + ' '.join(map(str, B)) + '\n'
    
    elif rule_type == "large":
        len_A = rng.randint(100, 1000)
        len_B = rng.randint(1, len_A)
        A, B = generate_arrays(len_A, len_B, -1000, 1000, rng)
        return ' '.join(map(str, A)) + '\n' + ' '.join(map(str, B)) + '\n'
    
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
