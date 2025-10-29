#!/usr/bin/env python3
"""
Test case generator for Simple Chatbot
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
    """Edge cases: single messages, each category"""
    cases = [
        # Single greeting
        "1\nhello",
        # Single farewell
        "1\nbye",
        # Single weather
        "1\nwhat is the weather",
        # Single name
        "1\nwho are you",
        # Single help
        "1\nhelp me",
        # Single unknown
        "1\nrandom text here"
    ]
    return random.choice(cases)

def generate_small_case():
    """Small cases: 2-10 messages with mixed categories"""
    n = random.randint(2, 10)
    
    greetings = ["hello", "hi", "hey", "hello there", "hi bot"]
    farewells = ["bye", "goodbye", "exit", "see you", "bye now"]
    weather = ["weather", "temperature", "forecast", "how is the weather", "tell me about the forecast"]
    names = ["name", "who are you", "what is your name", "tell me your name"]
    helps = ["help", "assist", "support", "can you help me", "I need support"]
    unknowns = ["what is AI", "tell me a joke", "random question", "how are you", "good morning"]
    
    all_messages = greetings + farewells + weather + names + helps + unknowns
    
    messages = random.sample(all_messages, min(n, len(all_messages)))
    
    lines = [str(n)]
    lines.extend(messages)
    
    return "\n".join(lines)

def generate_medium_case():
    """Medium cases: 11-30 messages"""
    n = random.randint(11, 30)
    
    message_pool = [
        # Greetings
        "hello", "hi", "hey", "hello there", "hi bot", "hey friend",
        # Farewells  
        "bye", "goodbye", "exit", "see you later", "bye now", "farewell",
        # Weather
        "weather", "temperature", "forecast", "how is the weather", 
        "tell me the temperature", "what's the forecast",
        # Names
        "name", "who are you", "what is your name", "introduce yourself",
        # Help
        "help", "assist me", "support", "can you help", "I need assistance",
        # Unknown
        "what is machine learning", "tell me about python", "how does AI work",
        "what is blockchain", "explain databases", "good morning", "how are you"
    ]
    
    messages = [random.choice(message_pool) for _ in range(n)]
    
    lines = [str(n)]
    lines.extend(messages)
    
    return "\n".join(lines)

def generate_large_case():
    """Large cases: 31-45 messages"""
    n = random.randint(31, 45)
    
    categories = {
        'greeting': ["hello", "hi", "hey", "hello world", "hi there", "hey bot"],
        'farewell': ["bye", "goodbye", "exit", "see you", "farewell", "bye bye"],
        'weather': ["weather today", "temperature now", "forecast this week", "is it sunny", "will it rain"],
        'name': ["your name", "who are you", "what's your name", "introduce yourself", "tell me about you"],
        'help': ["help me", "assist", "support needed", "can you help", "I need help"],
        'unknown': ["what is X", "tell me about Y", "how does Z work", "explain ABC", "random topic"]
    }
    
    messages = []
    for _ in range(n):
        category = random.choice(list(categories.keys()))
        messages.append(random.choice(categories[category]))
    
    lines = [str(n)]
    lines.extend(messages)
    
    return "\n".join(lines)

def generate_stress_case():
    """Stress cases: 46-50 messages with mixed content"""
    n = random.randint(46, 50)
    
    # Generate mix of all categories
    messages = []
    for _ in range(n):
        msg_type = random.randint(1, 6)
        if msg_type == 1:
            messages.append(random.choice(["hello", "hi", "hey"]))
        elif msg_type == 2:
            messages.append(random.choice(["bye", "goodbye", "exit"]))
        elif msg_type == 3:
            messages.append(random.choice(["weather", "temperature", "forecast"]))
        elif msg_type == 4:
            messages.append(random.choice(["name", "who are you"]))
        elif msg_type == 5:
            messages.append(random.choice(["help", "assist", "support"]))
        else:
            # Unknown with long text
            messages.append(f"unknown question number {_} with extra text" * random.randint(1, 3))
    
    lines = [str(n)]
    lines.extend(messages)
    
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate test case for simple chatbot')
    parser.add_argument('rule_type', choices=['edge_cases', 'small', 'medium', 'large', 'stress'])
    parser.add_argument('--args', type=json.loads, default='{}')
    parser.add_argument('--rng-seed', type=int, default=None)
    
    args_ns = parser.parse_args()
    if args_ns.rng_seed is not None:
        args_ns.args['seed'] = args_ns.rng_seed
    
    print(generate_case(args_ns.rule_type, args_ns.args), end='')
