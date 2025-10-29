import random
import json
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            (1, 1, 0.0),  # Single water
            (1, 1, 1.0),  # Single land
            (2, 2, 0.5),  # Tiny grid
            (3, 3, 0.3),  # Small grid sparse
            (5, 5, 0.0),  # All water
        ]
        m, n, land_prob = rng.choice(edge_types)
    
    elif rule_type == "small":
        m = rng.randint(2, 10)
        n = rng.randint(2, 10)
        land_prob = rng.uniform(0.2, 0.8)
    
    elif rule_type == "medium":
        m = rng.randint(10, 50)
        n = rng.randint(10, 50)
        land_prob = rng.uniform(0.3, 0.7)
    
    elif rule_type == "large":
        m = rng.randint(50, 150)
        n = rng.randint(50, 150)
        land_prob = rng.uniform(0.3, 0.6)
    
    elif rule_type == "stress":
        m = rng.randint(150, 300)
        n = rng.randint(150, 300)
        land_prob = rng.uniform(0.3, 0.5)
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Generate grid
    grid = []
    for _ in range(m):
        row = ''.join('1' if rng.random() < land_prob else '0' for _ in range(n))
        grid.append(row)
    
    # Format output
    output = f"{m} {n}\n"
    for row in grid:
        output += f"{row}\n"
    
    return output

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate test cases')
    parser.add_argument('rule_type', type=str, help='Type of test case to generate')
    parser.add_argument('--args', type=str, default='{}', help='Arguments as JSON string')
    parser.add_argument('--rng-seed', type=int, help='Random seed')
    
    args = parser.parse_args()
    
    test_args = json.loads(args.args)
    if args.rng_seed is not None:
        test_args['seed'] = args.rng_seed
    
    result = generate_case(args.rule_type, test_args)
    print(result, end='')
