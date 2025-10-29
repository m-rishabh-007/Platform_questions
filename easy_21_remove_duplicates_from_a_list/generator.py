# generator.py
import random
import sys

def generate():
    """
    Generates random test cases for Remove Duplicates from a List.
    """
    n = random.randint(5, 20)
    # Generate list with potential duplicates
    numbers = [random.randint(-50, 50) for _ in range(n)]
    
    # Remove duplicates preserving order
    seen = set()
    unique = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique.append(num)
    
    # Print input
    print(n)
    print(' '.join(map(str, numbers)))
    
    # Print expected output to stderr
    print(' '.join(map(str, unique)), file=sys.stderr)

if __name__ == "__main__":
    generate()
