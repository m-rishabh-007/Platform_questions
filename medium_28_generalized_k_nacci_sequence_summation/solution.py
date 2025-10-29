"""Reference implementation for the platform's official solution.

Update this file with the fully working algorithm that matches the
`description.txt` contract and is compatible with the wrappers.
"""

from __future__ import annotations

import sys
from typing import TextIO


class Solution:
    def sum_k_nacci_sequence(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n < 0:
            return 0
        
        # If n is less than k, we only have base cases (all 1s)
        if n < k:
            return n + 1
        
        # Initialize the first k terms (all 1s)
        terms = [1] * k
        total_sum = k  # Sum of first k terms
        
        # Calculate terms from index k to n
        for i in range(k, n + 1):
            # Calculate the next term as sum of previous k terms
            next_term = sum(terms)
            total_sum += next_term
            
            # Update the sliding window by shifting left and adding new term
            for j in range(k - 1):
                terms[j] = terms[j + 1]
            terms[k - 1] = next_term
        
        return total_sum


def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """Read from ``infile`` and write the answer to ``outfile``.

    This signature enables deterministic unit testing while still working with
    Judge0 (which provides stdin/stdout). Replace the body with the final
    algorithm for the problem, including any necessary parsing.
    """

    lines = infile.read().strip().split('\n')
    if len(lines) < 2:
        return

    n = int(lines[0])
    k = int(lines[1])
    
    solution = Solution()
    result = solution.sum_k_nacci_sequence(n, k)
    
    outfile.write(f"{result}\n")


if __name__ == "__main__":
    solve()