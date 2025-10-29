import random
import json
import sys
from collections import Counter

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            ([1], 1),
            ([1, 2], 1),
            ([1, 1, 2, 2, 3], 2),
            ([5, 5, 5, 5], 1),
            ([1, 2, 3, 4, 5], 5),
        ]
        nums, k = rng.choice(edge_types)
    
    elif rule_type == "small":
        n = rng.randint(1, 10)
        k = rng.randint(1, n)
        nums = [rng.randint(-100, 100) for _ in range(n)]
    
    elif rule_type == "medium":
        n = rng.randint(10, 100)
        k = rng.randint(1, min(20, n))
        nums = [rng.randint(-1000, 1000) for _ in range(n)]
    
    elif rule_type == "large":
        n = rng.randint(100, 1000)
        k = rng.randint(1, min(50, n))
        nums = [rng.randint(-10000, 10000) for _ in range(n)]
    
    elif rule_type == "stress":
        n = rng.randint(1000, 100000)
        k = rng.randint(1, min(100, n))
        nums = [rng.randint(-10000, 10000) for _ in range(n)]
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Format output
    output = f"{len(nums)} {k}\n"
    output += ' '.join(map(str, nums)) + '\n'
    
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
