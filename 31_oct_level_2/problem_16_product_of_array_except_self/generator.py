import random
import json
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            [1, 2],  # Minimal size
            [0, 0],  # All zeros
            [1, 0],  # One zero
            [-1, -2, -3],  # All negative
            [5, 5, 5, 5],  # All same
        ]
        nums = rng.choice(edge_types)
    
    elif rule_type == "small":
        n = rng.randint(2, 10)
        nums = [rng.randint(-30, 30) for _ in range(n)]
    
    elif rule_type == "medium":
        n = rng.randint(10, 100)
        nums = [rng.randint(-30, 30) for _ in range(n)]
    
    elif rule_type == "large":
        n = rng.randint(100, 1000)
        nums = [rng.randint(-30, 30) for _ in range(n)]
    
    elif rule_type == "stress":
        n = rng.randint(1000, 100000)
        nums = [rng.randint(-30, 30) for _ in range(n)]
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Format output
    output = f"{len(nums)}\n"
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
