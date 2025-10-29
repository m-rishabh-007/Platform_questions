#!/usr/bin/env python3
"""
Test case generator for Calendar/Appointment Scheduler CLI
Outputs INPUT only (orchestrator gets expected output from Judge0)
"""
import random
import argparse
import json
from datetime import datetime, timedelta

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
    """Edge cases: minimal operations, boundary conditions"""
    cases = [
        # Single ADD
        "1\nADD 2024-01-01 09:00 New Year meeting",
        # Single LIST (no appointments)
        "1\nLIST 2024-01-01",
        # Single DELETE (not found)
        "1\nDELETE 999",
        # ADD then immediate DELETE
        "2\nADD 2024-02-14 14:00 Valentine lunch\nDELETE 1",
        # Multiple LIST same date
        "3\nADD 2024-03-15 10:00 Meeting\nLIST 2024-03-15\nLIST 2024-03-15"
    ]
    return random.choice(cases)

def generate_small_case():
    """Small cases: 3-10 operations"""
    n = random.randint(3, 10)
    operations = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(n):
        op_type = random.choice(['ADD', 'LIST', 'DELETE'])
        
        if op_type == 'ADD':
            date_offset = random.randint(0, 30)
            date = (start_date + timedelta(days=date_offset)).strftime('%Y-%m-%d')
            hour = random.randint(8, 18)
            minute = random.choice([0, 15, 30, 45])
            time = f"{hour:02d}:{minute:02d}"
            desc = random.choice(['Meeting', 'Call', 'Review', 'Discussion', 'Presentation'])
            operations.append(f"ADD {date} {time} {desc}")
        elif op_type == 'LIST':
            date_offset = random.randint(0, 30)
            date = (start_date + timedelta(days=date_offset)).strftime('%Y-%m-%d')
            operations.append(f"LIST {date}")
        else:  # DELETE
            apt_id = random.randint(1, max(i, 5))
            operations.append(f"DELETE {apt_id}")
    
    return f"{n}\n" + "\n".join(operations)

def generate_medium_case():
    """Medium cases: 11-50 operations"""
    n = random.randint(11, 50)
    operations = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(n):
        op_type = random.choices(['ADD', 'LIST', 'DELETE'], weights=[50, 30, 20])[0]
        
        if op_type == 'ADD':
            date_offset = random.randint(0, 90)
            date = (start_date + timedelta(days=date_offset)).strftime('%Y-%m-%d')
            hour = random.randint(6, 22)
            minute = random.choice([0, 15, 30, 45])
            time = f"{hour:02d}:{minute:02d}"
            desc = random.choice([
                'Team standup', 'Client meeting', 'Code review', 
                'Planning session', 'Training', 'Workshop',
                'One-on-one', 'Demo', 'Sprint planning'
            ])
            operations.append(f"ADD {date} {time} {desc}")
        elif op_type == 'LIST':
            date_offset = random.randint(0, 90)
            date = (start_date + timedelta(days=date_offset)).strftime('%Y-%m-%d')
            operations.append(f"LIST {date}")
        else:  # DELETE
            apt_id = random.randint(1, max(i, 10))
            operations.append(f"DELETE {apt_id}")
    
    return f"{n}\n" + "\n".join(operations)

def generate_large_case():
    """Large cases: 51-80 operations"""
    n = random.randint(51, 80)
    operations = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(n):
        op_type = random.choices(['ADD', 'LIST', 'DELETE'], weights=[55, 25, 20])[0]
        
        if op_type == 'ADD':
            date_offset = random.randint(0, 180)
            date = (start_date + timedelta(days=date_offset)).strftime('%Y-%m-%d')
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            time = f"{hour:02d}:{minute:02d}"
            desc = f"Event_{i}_{random.randint(1000, 9999)}"
            operations.append(f"ADD {date} {time} {desc}")
        elif op_type == 'LIST':
            date_offset = random.randint(0, 180)
            date = (start_date + timedelta(days=date_offset)).strftime('%Y-%m-%d')
            operations.append(f"LIST {date}")
        else:  # DELETE
            apt_id = random.randint(1, max(i, 20))
            operations.append(f"DELETE {apt_id}")
    
    return f"{n}\n" + "\n".join(operations)

def generate_stress_case():
    """Stress cases: 81-100 operations, maximum complexity"""
    n = random.randint(81, 100)
    operations = []
    start_date = datetime(2024, 1, 1)
    
    # Heavy ADD bias for stress testing
    for i in range(n):
        op_type = random.choices(['ADD', 'LIST', 'DELETE'], weights=[60, 20, 20])[0]
        
        if op_type == 'ADD':
            date_offset = random.randint(0, 365)
            date = (start_date + timedelta(days=date_offset)).strftime('%Y-%m-%d')
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            time = f"{hour:02d}:{minute:02d}"
            # Long descriptions for stress
            desc = f"LongEventDescription_{i}_{'X' * random.randint(50, 90)}"
            operations.append(f"ADD {date} {time} {desc}")
        elif op_type == 'LIST':
            date_offset = random.randint(0, 365)
            date = (start_date + timedelta(days=date_offset)).strftime('%Y-%m-%d')
            operations.append(f"LIST {date}")
        else:  # DELETE
            apt_id = random.randint(1, max(i, 50))
            operations.append(f"DELETE {apt_id}")
    
    return f"{n}\n" + "\n".join(operations)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate test case for calendar scheduler')
    parser.add_argument('rule_type', choices=['edge_cases', 'small', 'medium', 'large', 'stress'])
    parser.add_argument('--args', type=json.loads, default='{}')
    parser.add_argument('--rng-seed', type=int, default=None)
    
    args_ns = parser.parse_args()
    if args_ns.rng_seed is not None:
        args_ns.args['seed'] = args_ns.rng_seed
    
    print(generate_case(args_ns.rule_type, args_ns.args), end='')
