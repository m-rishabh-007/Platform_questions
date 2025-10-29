# generator.py
import random
import sys

def generate():
    """
    Generates random test cases for Leap Year Checker.
    """
    # Generate random year
    year = random.randint(1800, 2100)
    
    # Check if leap year
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        is_leap = True
    else:
        is_leap = False
    
    # Print input
    print(year)
    
    # Print expected output to stderr
    print(is_leap, file=sys.stderr)

if __name__ == "__main__":
    generate()
