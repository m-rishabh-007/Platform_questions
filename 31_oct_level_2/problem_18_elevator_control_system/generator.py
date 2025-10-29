import random
import json
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_configs = [
            (5, 1, 2),   # Single elevator
            (10, 2, 3),  # Two elevators
            (3, 3, 1),   # More elevators than needed
            (20, 5, 5),  # Multiple elevators
            (10, 1, 1),  # Single request
        ]
        numFloors, numElevators, numRequests = rng.choice(edge_configs)
    
    elif rule_type == "small":
        numFloors = rng.randint(5, 10)
        numElevators = rng.randint(1, 3)
        numRequests = rng.randint(2, 5)
    
    elif rule_type == "medium":
        numFloors = rng.randint(10, 30)
        numElevators = rng.randint(2, 5)
        numRequests = rng.randint(5, 20)
    
    elif rule_type == "large":
        numFloors = rng.randint(30, 70)
        numElevators = rng.randint(3, 8)
        numRequests = rng.randint(20, 50)
    
    elif rule_type == "stress":
        numFloors = rng.randint(70, 100)
        numElevators = rng.randint(5, 10)
        numRequests = rng.randint(50, 100)
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Generate requests
    requests = []
    for _ in range(numRequests):
        if rng.random() < 0.5:  # EXTERNAL request
            floor = rng.randint(2, numFloors)
            direction = rng.choice(["UP", "DOWN"])
            requests.append(f"EXTERNAL {floor} {direction}")
        else:  # INTERNAL request
            elevator_id = rng.randint(0, numElevators - 1)
            dest = rng.randint(1, numFloors)
            requests.append(f"INTERNAL {elevator_id} {dest}")
    
    # Format output
    output = f"{numFloors} {numElevators} {numRequests}\n"
    for req in requests:
        output += f"{req}\n"
    
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
