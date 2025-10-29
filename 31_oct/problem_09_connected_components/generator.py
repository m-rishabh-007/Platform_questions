#!/usr/bin/env python3
"""
Test case generator for Connected Components in Undirected Graph
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
    """Edge cases: empty graph, single node, complete graph, no edges"""
    cases = [
        # Single node, no edges
        "1 0",
        # Multiple nodes, no edges
        "5 0",
        # Complete graph (all connected)
        "4 6\n0 1\n0 2\n0 3\n1 2\n1 3\n2 3",
        # Linear chain
        "5 4\n0 1\n1 2\n2 3\n3 4",
        # Star graph
        "6 5\n0 1\n0 2\n0 3\n0 4\n0 5"
    ]
    return random.choice(cases)

def generate_small_case():
    """Small cases: 2-20 nodes, sparse graphs"""
    n = random.randint(2, 20)
    m = random.randint(0, min(n * (n - 1) // 4, 30))
    
    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    
    lines = [f"{n} {m}"]
    for u, v in sorted(edges):
        lines.append(f"{u} {v}")
    
    return "\n".join(lines)

def generate_medium_case():
    """Medium cases: 21-100 nodes, medium density"""
    n = random.randint(21, 100)
    m = random.randint(n // 2, min(n * (n - 1) // 4, 500))
    
    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    
    lines = [f"{n} {m}"]
    for u, v in sorted(edges):
        lines.append(f"{u} {v}")
    
    return "\n".join(lines)

def generate_large_case():
    """Large cases: 101-500 nodes"""
    n = random.randint(101, 500)
    m = random.randint(n, min(n * (n - 1) // 4, 2000))
    
    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    
    lines = [f"{n} {m}"]
    for u, v in sorted(edges):
        lines.append(f"{u} {v}")
    
    return "\n".join(lines)

def generate_stress_case():
    """Stress cases: 501-1000 nodes, dense graphs"""
    n = random.randint(501, 1000)
    m = random.randint(n * 2, min(n * (n - 1) // 4, 5000))
    
    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    
    lines = [f"{n} {m}"]
    for u, v in sorted(edges):
        lines.append(f"{u} {v}")
    
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate test case for connected components')
    parser.add_argument('rule_type', choices=['edge_cases', 'small', 'medium', 'large', 'stress'])
    parser.add_argument('--args', type=json.loads, default='{}')
    parser.add_argument('--rng-seed', type=int, default=None)
    
    args_ns = parser.parse_args()
    if args_ns.rng_seed is not None:
        args_ns.args['seed'] = args_ns.rng_seed
    
    print(generate_case(args_ns.rule_type, args_ns.args), end='')
