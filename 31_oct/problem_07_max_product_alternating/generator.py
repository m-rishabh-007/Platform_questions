#!/usr/bin/env python3
"""
Test case generator for Maximum Product with Alternating Sum
Outputs INPUT only (orchestrator gets expected output from Judge0)
"""
import random
import argparse
import json

def generate_case(rule_type, args):
    """Generate a single test case based on rule type"""
    seed = args.get("seed")
    if seed is not None:
        random.seed(seed)
    
    if rule_type == "edge_cases":
        return generate_edge_case()
    elif rule_type == "small":
        return generate_small_case()
    elif rule_type == "medium":
        return generate_medium_case()
    elif rule_type == "large":
        return generate_large_case()
    elif rule_type == "stress":
        return generate_stress_case()
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")

def generate_edge_case():
    """Edge cases: minimal arrays, boundary k values"""
    cases = [
        # Single element, k=element value
        "1 5 100\n5",
        # Two elements, k=0 (equal)
        "2 0 50\n3 3",
        # All zeros
        "3 0 100\n0 0 0",
        # k unreachable
        "2 100 5000\n1 2",
        # Limit very small
        "3 5 2\n1 2 3"
    ]
    return random.choice(cases)

def generate_small_case():
    """Small cases: 1-10 elements"""
    n = random.randint(1, 10)
    k = random.randint(-50, 50)
    limit = random.randint(10, 500)
    
    nums = [random.randint(0, 12) for _ in range(n)]
    
    return f"{n} {k} {limit}\n" + " ".join(map(str, nums))

def generate_medium_case():
    """Medium cases: 11-50 elements"""
    n = random.randint(11, 50)
    k = random.randint(-500, 500)
    limit = random.randint(100, 2000)
    
    nums = [random.randint(0, 12) for _ in range(n)]
    
    return f"{n} {k} {limit}\n" + " ".join(map(str, nums))

def generate_large_case():
    """Large cases: 51-100 elements"""
    n = random.randint(51, 100)
    k = random.randint(-10000, 10000)
    limit = random.randint(500, 5000)
    
    nums = [random.randint(0, 12) for _ in range(n)]
    
    return f"{n} {k} {limit}\n" + " ".join(map(str, nums))

def generate_stress_case():
    """Stress cases: 101-150 elements, maximum complexity"""
    n = random.randint(101, 150)
    k = random.randint(-100000, 100000)
    limit = random.randint(1000, 5000)
    
    nums = [random.randint(0, 12) for _ in range(n)]
    
    return f"{n} {k} {limit}\n" + " ".join(map(str, nums))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate test case for max product alternating sum')
    parser.add_argument('rule_type', choices=['edge_cases', 'small', 'medium', 'large', 'stress'])
    parser.add_argument('--args', type=json.loads, default='{}')
    parser.add_argument('--rng-seed', type=int, default=None)
    
    args_ns = parser.parse_args()
    if args_ns.rng_seed is not None:
        args_ns.args['seed'] = args_ns.rng_seed
    
    print(generate_case(args_ns.rule_type, args_ns.args), end='')
