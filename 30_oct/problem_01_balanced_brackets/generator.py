import random
import sys

def generate_balanced_brackets(length, rng):
    """Generate a valid balanced bracket string"""
    if length == 0:
        return ""
    
    brackets = ['()', '[]', '{}']
    result = []
    stack = []
    
    for _ in range(length // 2):
        bracket_type = rng.choice(brackets)
        result.append(bracket_type[0])
        stack.append(bracket_type[1])
    
    while stack:
        result.append(stack.pop())
    
    return ''.join(result)

def generate_invalid_brackets(length, rng):
    """Generate an invalid bracket string"""
    if length == 0:
        return ")"
    
    brackets = ['(', ')', '[', ']', '{', '}']
    result = []
    
    for _ in range(length):
        result.append(rng.choice(brackets))
    
    # Force it to be invalid
    test_str = ''.join(result)
    if is_valid(test_str):
        if result:
            result[0] = ')'
    
    return ''.join(result)

def is_valid(s):
    """Check if bracket string is valid"""
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    
    return len(stack) == 0

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_cases = ["", "(", ")", "()", "[]", "{}", "((", "))", "([)]"]
        return rng.choice(edge_cases) + "\n"
    
    elif rule_type == "small":
        length = rng.randint(1, 10)
        if rng.random() < 0.5:
            return generate_balanced_brackets(length, rng) + "\n"
        else:
            return generate_invalid_brackets(length, rng) + "\n"
    
    elif rule_type == "medium":
        length = rng.randint(10, 100)
        if rng.random() < 0.5:
            return generate_balanced_brackets(length, rng) + "\n"
        else:
            return generate_invalid_brackets(length, rng) + "\n"
    
    elif rule_type == "large":
        length = rng.randint(100, 1000)
        if rng.random() < 0.5:
            return generate_balanced_brackets(length, rng) + "\n"
        else:
            return generate_invalid_brackets(length, rng) + "\n"
    
    elif rule_type == "stress":
        length = rng.randint(1000, 10000)
        if rng.random() < 0.5:
            return generate_balanced_brackets(length, rng) + "\n"
        else:
            return generate_invalid_brackets(length, rng) + "\n"
    
    raise ValueError(f"Unhandled rule_type: {rule_type}")

if __name__ == "__main__":
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("rule_type")
    parser.add_argument("--args", type=json.loads, default="{}")
    parser.add_argument("--rng-seed", type=int, default=None)
    ns = parser.parse_args()
    if ns.rng_seed is not None:
        ns.args["seed"] = ns.rng_seed
    print(generate_case(ns.rule_type, ns.args), end="")
