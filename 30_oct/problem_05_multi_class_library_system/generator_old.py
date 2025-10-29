import random
import json
import sys

# Sample book titles and authors
BOOK_TITLES = [
    ("Dune", "Frank Herbert"),
    ("1984", "George Orwell"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("Pride and Prejudice", "Jane Austen"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("Brave New World", "Aldous Huxley"),
    ("Animal Farm", "George Orwell"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Fahrenheit 451", "Ray Bradbury")
]

MEMBER_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry", "Iris", "Jack"]

def generate_random_commands(num_commands, rng):
    """Generate random library commands"""
    commands = []
    books_added = []
    members_added = []
    
    # Add some books and members first
    num_books = min(num_commands // 4, len(BOOK_TITLES))
    num_members = min(num_commands // 4, len(MEMBER_NAMES))
    
    for i in range(num_books):
        title, author = BOOK_TITLES[i]
        commands.append(f'ADD BOOK "{title}" "{author}"')
        books_added.append(title)
    
    for i in range(num_members):
        name = MEMBER_NAMES[i]
        member_id = (i + 1) * 100 + rng.randint(1, 99)
        commands.append(f'ADD MEMBER "{name}" {member_id}')
        members_added.append(member_id)
    
    # Generate remaining commands
    for _ in range(num_commands - len(commands)):
        cmd_type = rng.choice(['ADD_BOOK', 'ADD_MEMBER', 'CHECKOUT', 'RETURN'])
        
        if cmd_type == 'ADD_BOOK':
            title, author = rng.choice(BOOK_TITLES)
            commands.append(f'ADD BOOK "{title}" "{author}"')
            if title not in books_added:
                books_added.append(title)
                
        elif cmd_type == 'ADD_MEMBER':
            name = rng.choice(MEMBER_NAMES)
            member_id = rng.randint(1, 1000)
            commands.append(f'ADD MEMBER "{name}" {member_id}')
            if member_id not in members_added:
                members_added.append(member_id)
                
        elif cmd_type == 'CHECKOUT' and books_added and members_added:
            title = rng.choice(books_added)
            member_id = rng.choice(members_added)
            commands.append(f'CHECKOUT {member_id} "{title}"')
            
        elif cmd_type == 'RETURN' and books_added:
            title = rng.choice(books_added)
            commands.append(f'RETURN "{title}"')
    
    return commands

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_cases = [
            ['ADD BOOK "Test" "Author"'],
            ['ADD MEMBER "Alice" 1'],
            ['ADD BOOK "Book1" "Author1"', 'ADD BOOK "Book1" "Author1"'],
            ['CHECKOUT 999 "NonExistent"'],
            ['RETURN "NonExistent"'],
        ]
        commands = rng.choice(edge_cases)
        commands.append('EXIT')
        return '\n'.join(commands) + '\n'
    
    elif rule_type == "small":
        num_commands = rng.randint(5, 15)
        commands = generate_random_commands(num_commands, rng)
        commands.append('EXIT')
        return '\n'.join(commands) + '\n'
    
    elif rule_type == "medium":
        num_commands = rng.randint(15, 50)
        commands = generate_random_commands(num_commands, rng)
        commands.append('EXIT')
        return '\n'.join(commands) + '\n'
    
    elif rule_type == "large":
        num_commands = rng.randint(50, 200)
        commands = generate_random_commands(num_commands, rng)
        commands.append('EXIT')
        return '\n'.join(commands) + '\n'
    
    raise ValueError(f"Unhandled rule_type: {rule_type}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("rule_type")
    parser.add_argument("--args", type=json.loads, default="{}")
    parser.add_argument("--rng-seed", type=int, default=None)
    ns = parser.parse_args()
    if ns.rng_seed is not None:
        ns.args["seed"] = ns.rng_seed
    print(generate_case(ns.rule_type, ns.args), end="")
    """Simulate library operations and return output"""
    books = {}
    members = {}
    output = []
    
    for cmd in commands:
        parts = cmd.split()
        
        if parts[0] == "ADD" and parts[1] == "BOOK":
            # Extract quoted strings
            title = cmd.split('"')[1]
            author = cmd.split('"')[3]
            
            if title not in books:
                books[title] = {'author': author, 'checked_out': False, 'by': None}
                output.append(f'Book "{title}" added.')
                
        elif parts[0] == "ADD" and parts[1] == "MEMBER":
            name = cmd.split('"')[1]
            member_id = int(cmd.split('"')[2].strip())
            
            if member_id not in members:
                members[member_id] = name
                output.append(f'Member "{name}" registered.')
                
        elif parts[0] == "CHECKOUT":
            member_id = int(parts[1])
            title = cmd.split('"')[1]
            
            if member_id not in members:
                output.append("Error: Member not found.")
            elif title not in books:
                output.append("Error: Book not found.")
            elif books[title]['checked_out']:
                output.append("Error: Book not available.")
            else:
                books[title]['checked_out'] = True
                books[title]['by'] = member_id
                output.append("Checkout successful.")
                
        elif parts[0] == "RETURN":
            title = cmd.split('"')[1]
            
            if title not in books or not books[title]['checked_out']:
                output.append("Error: Book not in records or was not checked out.")
            else:
                books[title]['checked_out'] = False
                books[title]['by'] = None
                output.append("Return successful.")
    
    return '\n'.join(output)

def generate_test_case(rule_type):
    """Generate a test case based on rule type"""
    
    if rule_type == "example":
        commands = [
            'ADD BOOK "Dune" "Frank Herbert"',
            'ADD MEMBER "Bob" 101',
            'CHECKOUT 101 "Dune"',
            'CHECKOUT 101 "Dune"',
            'RETURN "Dune"',
            'EXIT'
        ]
        test_input = '\n'.join(commands)
        expected = simulate_library(commands[:-1])
        return {"input": test_input, "output": expected}
    
    elif rule_type == "edge":
        edge_cases = [
            ['ADD BOOK "Test" "Author"', 'EXIT'],
            ['ADD MEMBER "Alice" 1', 'EXIT'],
            ['ADD BOOK "Book1" "Author1"', 'ADD BOOK "Book1" "Author1"', 'EXIT'],
            ['CHECKOUT 999 "NonExistent"', 'EXIT'],
            ['RETURN "NonExistent"', 'EXIT'],
        ]
        commands = random.choice(edge_cases)
        test_input = '\n'.join(commands)
        expected = simulate_library(commands[:-1])
        return {"input": test_input, "output": expected}
    
    elif rule_type == "small":
        num_commands = random.randint(5, 15)
        commands = generate_random_commands(num_commands)
        commands.append('EXIT')
        test_input = '\n'.join(commands)
        expected = simulate_library(commands[:-1])
        return {"input": test_input, "output": expected}
    
    elif rule_type == "medium":
        num_commands = random.randint(15, 50)
        commands = generate_random_commands(num_commands)
        commands.append('EXIT')
        test_input = '\n'.join(commands)
        expected = simulate_library(commands[:-1])
        return {"input": test_input, "output": expected}
    
    elif rule_type == "large":
        num_commands = random.randint(50, 100)
        commands = generate_random_commands(num_commands)
        commands.append('EXIT')
        test_input = '\n'.join(commands)
        expected = simulate_library(commands[:-1])
        return {"input": test_input, "output": expected}
    
    elif rule_type == "stress":
        num_commands = random.randint(100, 200)
        commands = generate_random_commands(num_commands)
        commands.append('EXIT')
        test_input = '\n'.join(commands)
        expected = simulate_library(commands[:-1])
        return {"input": test_input, "output": expected}
    
    return {"input": "EXIT", "output": ""}

def generate_random_commands(num_commands):
    """Generate random library commands"""
    commands = []
    books_added = []
    members_added = []
    
    # Add some books and members first
    num_books = min(num_commands // 4, len(BOOK_TITLES))
    num_members = min(num_commands // 4, len(MEMBER_NAMES))
    
    for i in range(num_books):
        title, author = BOOK_TITLES[i]
        commands.append(f'ADD BOOK "{title}" "{author}"')
        books_added.append(title)
    
    for i in range(num_members):
        name = MEMBER_NAMES[i]
        member_id = (i + 1) * 100 + random.randint(1, 99)
        commands.append(f'ADD MEMBER "{name}" {member_id}')
        members_added.append(member_id)
    
    # Generate remaining commands
    for _ in range(num_commands - len(commands)):
        cmd_type = random.choice(['ADD_BOOK', 'ADD_MEMBER', 'CHECKOUT', 'RETURN'])
        
        if cmd_type == 'ADD_BOOK':
            title, author = random.choice(BOOK_TITLES)
            commands.append(f'ADD BOOK "{title}" "{author}"')
            if title not in books_added:
                books_added.append(title)
                
        elif cmd_type == 'ADD_MEMBER':
            name = random.choice(MEMBER_NAMES)
            member_id = random.randint(1, 1000)
            commands.append(f'ADD MEMBER "{name}" {member_id}')
            if member_id not in members_added:
                members_added.append(member_id)
                
        elif cmd_type == 'CHECKOUT' and books_added and members_added:
            title = random.choice(books_added)
            member_id = random.choice(members_added)
            commands.append(f'CHECKOUT {member_id} "{title}"')
            
        elif cmd_type == 'RETURN' and books_added:
            title = random.choice(books_added)
            commands.append(f'RETURN "{title}"')
    
    return commands

if __name__ == "__main__":
    # Load config
    with open("config.json", "r") as f:
        config = json.load(f)
    
    test_cases = []
    
    for rule_type, count in config["test_cases"].items():
        for _ in range(count):
            test_cases.append(generate_test_case(rule_type))
    
    # Save test cases
    with open("test_cases.json", "w") as f:
        json.dump(test_cases, f, indent=2)
    
    print(f"Generated {len(test_cases)} test cases")
