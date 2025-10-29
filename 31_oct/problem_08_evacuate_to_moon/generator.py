#!/usr/bin/env python3
"""
Test case generator for Evacuate to Moon
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
    """Edge cases: minimal test cases, boundary conditions"""
    cases = [
        # Single car, single outlet
        "1\n1 1 1\n100\n50",
        # More cars than outlets
        "1\n3 1 1\n10 20 30\n50",
        # More outlets than cars
        "1\n1 3 1\n100\n10 20 30",
        # Zero hours
        "1\n2 2 0\n100 100\n50 50",
        # Capacity much less than generated
        "1\n1 1 10\n10\n100"
    ]
    return random.choice(cases)

def generate_small_case():
    """Small cases: 1-3 test cases, 1-5 cars/outlets"""
    t = random.randint(1, 3)
    lines = [str(t)]
    
    for _ in range(t):
        n = random.randint(1, 5)
        m = random.randint(1, 5)
        h = random.randint(1, 10)
        
        lines.append(f"{n} {m} {h}")
        
        capacity = [random.randint(10, 100) for _ in range(n)]
        lines.append(" ".join(map(str, capacity)))
        
        power = [random.randint(5, 50) for _ in range(m)]
        lines.append(" ".join(map(str, power)))
    
    return "\n".join(lines)

def generate_medium_case():
    """Medium cases: 4-10 test cases, 6-20 cars/outlets"""
    t = random.randint(4, 10)
    lines = [str(t)]
    
    for _ in range(t):
        n = random.randint(6, 20)
        m = random.randint(6, 20)
        h = random.randint(10, 50)
        
        lines.append(f"{n} {m} {h}")
        
        capacity = [random.randint(100, 1000) for _ in range(n)]
        lines.append(" ".join(map(str, capacity)))
        
        power = [random.randint(50, 500) for _ in range(m)]
        lines.append(" ".join(map(str, power)))
    
    return "\n".join(lines)

def generate_large_case():
    """Large cases: 11-50 test cases, 21-50 cars/outlets"""
    t = random.randint(11, 50)
    lines = [str(t)]
    
    for _ in range(t):
        n = random.randint(21, 50)
        m = random.randint(21, 50)
        h = random.randint(50, 100)
        
        lines.append(f"{n} {m} {h}")
        
        capacity = [random.randint(1000, 10000) for _ in range(n)]
        lines.append(" ".join(map(str, capacity)))
        
        power = [random.randint(500, 5000) for _ in range(m)]
        lines.append(" ".join(map(str, power)))
    
    return "\n".join(lines)

def generate_stress_case():
    """Stress cases: many test cases with large arrays"""
    t = random.randint(50, 100)
    lines = [str(t)]
    
    for _ in range(t):
        n = random.randint(80, 100)
        m = random.randint(80, 100)
        h = random.randint(90, 100)
        
        lines.append(f"{n} {m} {h}")
        
        capacity = [random.randint(10000, 100000) for _ in range(n)]
        lines.append(" ".join(map(str, capacity)))
        
        power = [random.randint(10000, 100000) for _ in range(m)]
        lines.append(" ".join(map(str, power)))
    
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate test case for evacuate to moon')
    parser.add_argument('rule_type', choices=['edge_cases', 'small', 'medium', 'large', 'stress'])
    parser.add_argument('--args', type=json.loads, default='{}')
    parser.add_argument('--rng-seed', type=int, default=None)
    
    args_ns = parser.parse_args()
    if args_ns.rng_seed is not None:
        args_ns.args['seed'] = args_ns.rng_seed
    
    print(generate_case(args_ns.rule_type, args_ns.args), end='')
