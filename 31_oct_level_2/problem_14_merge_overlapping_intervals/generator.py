import random
import json
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            [(1, 1)],  # Single interval
            [(1, 2), (3, 4)],  # No overlap
            [(1, 5), (2, 3)],  # Nested
            [(1, 3), (2, 4), (3, 5)],  # Chain overlap
            [(1, 10)],  # Single large interval
        ]
        intervals = rng.choice(edge_types)
        
    elif rule_type == "small":
        n = rng.randint(1, 5)
        intervals = []
        for _ in range(n):
            start = rng.randint(0, 50)
            end = rng.randint(start + 1, start + 20)
            intervals.append((start, end))
    
    elif rule_type == "medium":
        n = rng.randint(5, 50)
        intervals = []
        for _ in range(n):
            start = rng.randint(0, 500)
            end = rng.randint(start + 1, start + 100)
            intervals.append((start, end))
    
    elif rule_type == "large":
        n = rng.randint(50, 1000)
        intervals = []
        for _ in range(n):
            start = rng.randint(0, 5000)
            end = rng.randint(start + 1, start + 200)
            intervals.append((start, end))
    
    elif rule_type == "stress":
        n = rng.randint(1000, 10000)
        intervals = []
        for _ in range(n):
            start = rng.randint(0, 9500)
            end = rng.randint(start + 1, min(start + 500, 10000))
            intervals.append((start, end))
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Format output
    output = f"{len(intervals)}\n"
    for start, end in intervals:
        output += f"{start} {end}\n"
    
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
