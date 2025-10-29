"""Reference implementation for the platform's official solution.

Update this file with the fully working algorithm that matches the
`description.txt` contract and is compatible with the wrappers.
"""

from __future__ import annotations

import sys
from typing import TextIO


class Solution:
    def capitalizeWords(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        capitalized_words = []
        for word in words:
            if word:  # Check if word is not empty
                capitalized_word = word[0].upper() + word[1:].lower() if len(word) > 1 else word.upper()
                capitalized_words.append(capitalized_word)
        return ' '.join(capitalized_words)


def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """Read from ``infile`` and write the answer to ``outfile``.

    This signature enables deterministic unit testing while still working with
    Judge0 (which provides stdin/stdout). Replace the body with the final
    algorithm for the problem, including any necessary parsing.
    """

    sentence = infile.read().strip()
    
    # Create solution instance and call the method
    solution = Solution()
    result = solution.capitalizeWords(sentence)
    
    # Output the result
    outfile.write(f"{result}\n")


if __name__ == "__main__":
    solve()
