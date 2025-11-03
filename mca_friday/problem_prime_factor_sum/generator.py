#!/usr/bin/env python3
import random
import argparse
import json
import sys

def generate_edge_cases(args, rng):
    """Generate edge case inputs"""
    cases = [2, 3, 5, 7, 11, 13]
    return str(rng.choice(cases))

def generate_small(args, rng):
    """Generate small test case"""
    n = rng.randint(2, 100)
    return str(n)

def generate_medium(args, rng):
    """Generate medium test case"""
    n = rng.randint(100, 10000)
    return str(n)

def generate_large(args, rng):
    """Generate large test case"""
    n = rng.randint(10000, 1000000)
    return str(n)

def generate_stress(args, rng):
    """Generate stress test case"""
    n = rng.randint(1000000, 1000000000)
    return str(n)

def main():
    parser = argparse.ArgumentParser(description='Generate test cases for Prime Factor Sum')
    parser.add_argument('rule_type', choices=['edge_cases', 'small', 'medium', 'large', 'stress'])
    parser.add_argument('--args', type=str, default='{}')
    parser.add_argument('--rng-seed', type=int, default=None)
    
    args = parser.parse_args()
    rule_args = json.loads(args.args)
    
    rng = random.Random(args.rng_seed)
    
    generators = {
        'edge_cases': generate_edge_cases,
        'small': generate_small,
        'medium': generate_medium,
        'large': generate_large,
        'stress': generate_stress
    }
    
    test_input = generators[args.rule_type](rule_args, rng)
    print(test_input)

if __name__ == '__main__':
    main()
