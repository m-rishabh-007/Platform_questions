#!/usr/bin/env python3
"""
Test case generator for Lowest Common Ancestor
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

def generate_tree(n):
    """Generate random tree structure"""
    lines = [str(n)]
    
    # Root node
    root_value = random.randint(-1000, 1000)
    lines.append(f"0 -1 {root_value}")
    
    # Other nodes
    values = set([root_value])
    for i in range(1, n):
        parent_id = random.randint(0, i - 1)
        value = random.randint(-1000, 1000)
        while value in values:
            value = random.randint(-1000, 1000)
        values.add(value)
        lines.append(f"{i} {parent_id} {value}")
    
    # Pick two random nodes (not root)
    if n >= 3:
        node_values = list(values)
        p, q = random.sample(node_values, 2)
    elif n == 2:
        p, q = list(values)
    else:
        p = q = root_value
    
    lines.append(f"{p} {q}")
    
    return "\n".join(lines)

def generate_edge_case():
    """Edge cases: minimal trees"""
    cases = [
        # Two nodes
        "2\n0 -1 10\n1 0 20\n10 20",
        # Three nodes, linear
        "3\n0 -1 1\n1 0 2\n2 1 3\n2 3",
        # Three nodes, branching
        "3\n0 -1 5\n1 0 3\n2 0 7\n3 7"
    ]
    return random.choice(cases)

def generate_small_case():
    """Small cases: 2-10 nodes"""
    n = random.randint(2, 10)
    return generate_tree(n)

def generate_medium_case():
    """Medium cases: 11-50 nodes"""
    n = random.randint(11, 50)
    return generate_tree(n)

def generate_large_case():
    """Large cases: 51-200 nodes"""
    n = random.randint(51, 200)
    return generate_tree(n)

def generate_stress_case():
    """Stress cases: 201-1000 nodes"""
    n = random.randint(201, 1000)
    return generate_tree(n)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate test case for LCA')
    parser.add_argument('rule_type', choices=['edge_cases', 'small', 'medium', 'large', 'stress'])
    parser.add_argument('--args', type=json.loads, default='{}')
    parser.add_argument('--rng-seed', type=int, default=None)
    
    args_ns = parser.parse_args()
    if args_ns.rng_seed is not None:
        args_ns.args['seed'] = args_ns.rng_seed
    
    print(generate_case(args_ns.rule_type, args_ns.args), end='')
