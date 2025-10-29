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
