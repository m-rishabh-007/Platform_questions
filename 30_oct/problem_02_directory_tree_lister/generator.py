import random
import json
import string
import sys

def generate_name(rng):
    """Generate a random file or directory name"""
    length = rng.randint(3, 12)
    chars = string.ascii_lowercase + string.digits + '_'
    name = ''.join(rng.choice(chars) for _ in range(length))
    
    # Add extension for files sometimes
    if rng.random() < 0.5:
        extensions = ['.txt', '.py', '.cpp', '.md', '.json', '.js']
        name += rng.choice(extensions)
    
    return name

def generate_filesystem(max_depth, current_depth, max_items, rng):
    """Generate a random filesystem structure"""
    if current_depth >= max_depth:
        return None
    
    fs = {}
    num_items = rng.randint(1, min(max_items, 10))
    
    for _ in range(num_items):
        name = generate_name(rng)
        
        # Decide if it's a directory or file
        if current_depth < max_depth - 1 and rng.random() < 0.4:
            # It's a directory
            fs[name] = generate_filesystem(max_depth, current_depth + 1, max_items, rng)
        else:
            # It's a file
            fs[name] = None
    
    return fs

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_cases = [
            {},
            {"file.txt": None},
            {"dir": {}},
            {"a.txt": None, "b.txt": None},
            {"nested": {"deep": {"file.txt": None}}}
        ]
        fs = rng.choice(edge_cases)
        return json.dumps(fs) + "\n"
    
    elif rule_type == "small":
        max_depth = rng.randint(1, 3)
        fs = generate_filesystem(max_depth, 0, 5, rng)
        return json.dumps(fs) + "\n"
    
    elif rule_type == "medium":
        max_depth = rng.randint(3, 5)
        fs = generate_filesystem(max_depth, 0, 8, rng)
        return json.dumps(fs) + "\n"
    
    elif rule_type == "large":
        max_depth = rng.randint(5, 8)
        fs = generate_filesystem(max_depth, 0, 12, rng)
        return json.dumps(fs) + "\n"
    
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
