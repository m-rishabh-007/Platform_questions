# generator.py
import random
import sys
import string

def generate():
    """
    Generates random test cases for Capitalize First Letter of Each Word.
    """
    # Generate random sentence
    num_words = random.randint(1, 8)
    words = []
    for _ in range(num_words):
        word_length = random.randint(2, 10)
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        words.append(word)
    
    sentence = ' '.join(words)
    capitalized = ' '.join(word.capitalize() for word in words)
    
    # Print input
    print(sentence)
    
    # Print expected output to stderr
    print(capitalized, file=sys.stderr)

if __name__ == "__main__":
    generate()
