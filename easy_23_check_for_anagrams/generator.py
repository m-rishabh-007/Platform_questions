# generator.py
import random
import sys
import string

def generate():
    """
    Generates random test cases for Check for Anagrams.
    """
    # 60% chance they're anagrams
    if random.random() < 0.6:
        # Generate first string
        length = random.randint(3, 15)
        str1 = ''.join(random.choices(string.ascii_lowercase, k=length))
        # Create anagram by shuffling
        str2_list = list(str1)
        random.shuffle(str2_list)
        str2 = ''.join(str2_list)
        result = True
    else:
        # Generate two different strings
        length1 = random.randint(3, 15)
        length2 = random.randint(3, 15)
        str1 = ''.join(random.choices(string.ascii_lowercase, k=length1))
        str2 = ''.join(random.choices(string.ascii_uppercase, k=length2))
        # Check if they're accidentally anagrams
        result = sorted(str1.lower().replace(' ', '')) == sorted(str2.lower().replace(' ', ''))
    
    # Print input
    print(str1)
    print(str2)
    
    # Print expected output to stderr
    print(result, file=sys.stderr)

if __name__ == "__main__":
    generate()
