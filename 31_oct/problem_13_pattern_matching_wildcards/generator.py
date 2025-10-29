#!/usr/bin/env python3
"""
Test case generator for Pattern Matching with Wildcards
Outputs INPUT only (single test case)
"""

import random
import argparse
import json

def generate_test_case(rule_type, args, rng_seed):
    random.seed(rng_seed)
    
    def random_string(length):
        """Generate random lowercase string"""
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))
    
    def create_matching_pattern(s):
        """Create a pattern that matches string s"""
        if not s:
            return '*' if random.random() < 0.5 else ''
        
        pattern = []
        i = 0
        while i < len(s):
            choice = random.random()
            if choice < 0.3:  # Use exact character
                pattern.append(s[i])
                i += 1
            elif choice < 0.6:  # Use ?
                pattern.append('?')
                i += 1
            else:  # Use * for one or more characters
                pattern.append('*')
                skip = random.randint(1, min(5, len(s) - i))
                i += skip
        
        # Sometimes add trailing *
        if random.random() < 0.3:
            pattern.append('*')
        
        return ''.join(pattern)
    
    def create_non_matching_pattern(s):
        """Create a pattern that doesn't match string s"""
        if not s:
            return random_string(random.randint(1, 5))
        
        # Several strategies for non-matching
        strategy = random.choice(['different_char', 'wrong_length', 'incompatible'])
        
        if strategy == 'different_char':
            # Change one specific character match to wrong one
            pattern = list(s)
            idx = random.randint(0, len(s) - 1)
            pattern[idx] = chr((ord(s[idx]) - ord('a') + 1) % 26 + ord('a'))
            return ''.join(pattern)
        elif strategy == 'wrong_length':
            # Pattern forces specific length that doesn't match
            return '?' * (len(s) + random.randint(1, 3))
        else:  # incompatible
            # Create pattern with characters not in s
            chars_not_in_s = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in s]
            if chars_not_in_s:
                return random.choice(chars_not_in_s) + '*'
            else:
                return '?' * (len(s) + 1)
    
    if rule_type == "edge_cases":
        # Edge cases: empty strings, only wildcards, etc.
        test_type = random.choice([
            "both_empty",
            "empty_string_star",
            "empty_pattern",
            "only_stars",
            "only_questions"
        ])
        
        if test_type == "both_empty":
            s, p = "", ""
        elif test_type == "empty_string_star":
            s = ""
            p = '*' * random.randint(1, 3)
        elif test_type == "empty_pattern":
            s = random_string(random.randint(1, 5))
            p = ""
        elif test_type == "only_stars":
            length = random.randint(1, 10)
            s = random_string(length)
            p = '*' * random.randint(1, 5)
        else:  # only_questions
            length = random.randint(1, 10)
            s = random_string(length)
            p = '?' * length if random.random() < 0.5 else '?' * (length + 1)
    
    elif rule_type == "small":
        s_len = random.randint(1, 20)
        s = random_string(s_len)
        
        if random.random() < 0.5:
            p = create_matching_pattern(s)
        else:
            p = create_non_matching_pattern(s)
    
    elif rule_type == "medium":
        s_len = random.randint(50, 200)
        s = random_string(s_len)
        
        if random.random() < 0.5:
            p = create_matching_pattern(s)
        else:
            p = create_non_matching_pattern(s)
    
    elif rule_type == "large":
        s_len = random.randint(500, 1000)
        s = random_string(s_len)
        
        # For large cases, use simpler patterns
        if random.random() < 0.5:
            # Matching with stars
            p = '*' + s[len(s)//2:len(s)//2+5] + '*'
        else:
            # Non-matching
            p = '*' + random_string(5) + '*' + random_string(5)
    
    elif rule_type == "stress":
        s_len = random.randint(1500, 2000)
        s = random_string(s_len)
        
        # Stress with many stars or questions
        p_len = random.randint(100, 500)
        p = ''.join(random.choice('*?') for _ in range(p_len))
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Output format: s on first line, p on second line
    print(s)
    print(p)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate test case for Pattern Matching with Wildcards')
    parser.add_argument('rule_type', help='Type of test case to generate')
    parser.add_argument('--args', default='{}', help='Additional arguments as JSON')
    parser.add_argument('--rng-seed', type=int, default=None, help='Random seed')
    
    args_parsed = parser.parse_args()
    args_dict = json.loads(args_parsed.args)
    
    seed = args_parsed.rng_seed if args_parsed.rng_seed is not None else random.randint(1, 1000000)
    generate_test_case(args_parsed.rule_type, args_dict, seed)
