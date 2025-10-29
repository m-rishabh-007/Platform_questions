# generator.py
import random
import sys

def generate():
    """
    Generates random test cases for Simple Interest Calculator.
    """
    # Generate random principal, rate, and time
    principal = random.uniform(1000, 100000)
    rate = random.uniform(1, 20)
    time = random.uniform(0.5, 10)
    
    # Calculate simple interest
    simple_interest = (principal * rate * time) / 100
    
    # Print input
    print(f"{principal:.2f} {rate:.2f} {time:.2f}")
    
    # Print expected output to stderr
    print(f"{simple_interest:.2f}", file=sys.stderr)

if __name__ == "__main__":
    generate()
