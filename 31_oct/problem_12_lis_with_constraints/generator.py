#!/usr/bin/env python3
"""
Test case generator for Longest Increasing Subsequence with Constraints
Outputs INPUT only (single test case)
"""

import random
import argparse
import json

def generate_test_case(rule_type, args, rng_seed):
    random.seed(rng_seed)
    
    if rule_type == "edge_cases":
        # Edge cases: small n, specific k values
        test_type = random.choice([
            "single_element",
            "all_same",
            "all_decreasing",
            "k_is_1",
            "k_very_large"
        ])
        
        if test_type == "single_element":
            n, k = 1, random.randint(1, 100)
            nums = [random.randint(-1000, 1000)]
        elif test_type == "all_same":
            n = random.randint(2, 5)
            k = random.randint(1, 100)
            val = random.randint(-1000, 1000)
            nums = [val] * n
        elif test_type == "all_decreasing":
            n = random.randint(3, 5)
            k = random.randint(1, 100)
            nums = sorted([random.randint(-1000, 1000) for _ in range(n)], reverse=True)
        elif test_type == "k_is_1":
            n = random.randint(3, 5)
            k = 1
            nums = [random.randint(1, 20) for _ in range(n)]
        else:  # k_very_large
            n = random.randint(3, 5)
            k = 10**9
            nums = [random.randint(-1000, 1000) for _ in range(n)]
    
    elif rule_type == "small":
        n = random.randint(5, 20)
        k = random.randint(1, 100)
        nums = [random.randint(-100, 100) for _ in range(n)]
    
    elif rule_type == "medium":
        n = random.randint(50, 200)
        k = random.randint(1, 1000)
        nums = [random.randint(-10000, 10000) for _ in range(n)]
    
    elif rule_type == "large":
        n = random.randint(500, 1000)
        k = random.randint(1, 100000)
        nums = [random.randint(-100000, 100000) for _ in range(n)]
    
    elif rule_type == "stress":
        n = random.randint(1500, 2000)
        k = random.randint(1, 10**9)
        nums = [random.randint(-10**9, 10**9) for _ in range(n)]
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Output format: n k, then array
    print(f"{n} {k}")
    print(" ".join(map(str, nums)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate test case for LIS with Constraints')
    parser.add_argument('rule_type', help='Type of test case to generate')
    parser.add_argument('--args', default='{}', help='Additional arguments as JSON')
    parser.add_argument('--rng-seed', type=int, default=None, help='Random seed')
    
    args_parsed = parser.parse_args()
    args_dict = json.loads(args_parsed.args)
    
    seed = args_parsed.rng_seed if args_parsed.rng_seed is not None else random.randint(1, 1000000)
    generate_test_case(args_parsed.rule_type, args_dict, seed)
