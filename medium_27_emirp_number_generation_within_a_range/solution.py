"""Reference implementation for the platform's official solution.

Update this file with the fully working algorithm that matches the
`description.txt` contract and is compatible with the wrappers.
"""

from __future__ import annotations

import sys
from typing import TextIO


class Solution:
    def find_emirps_in_range(self, limit):
        """
        :type limit: int
        :rtype: List[int]
        """
        if limit < 13:  # Smallest Emirp is 13
            return []
        
        # Generate all primes up to limit using Sieve of Eratosthenes
        primes = self._sieve_of_eratosthenes(limit)
        
        emirps = []
        
        for prime in primes:
            if prime < 10:  # Skip single-digit primes
                continue
                
            # Reverse the digits
            reversed_num = self._reverse_digits(prime)
            
            # Check if the reversed number is different and also prime
            if reversed_num != prime and self._is_prime(reversed_num):
                emirps.append(prime)
        
        return sorted(emirps)
    
    def _sieve_of_eratosthenes(self, n):
        """Generate all prime numbers up to n using Sieve of Eratosthenes"""
        if n < 2:
            return []
        
        # Create a boolean array and initialize all entries as True
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        p = 2
        while p * p <= n:
            if is_prime[p]:
                # Update all multiples of p
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        
        # Collect all prime numbers
        primes = []
        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)
        
        return primes
    
    def _reverse_digits(self, num):
        """Reverse the digits of a number"""
        return int(str(num)[::-1])
    
    def _is_prime(self, n):
        """Check if a number is prime"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Check odd divisors up to sqrt(n)
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True


def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """Read from ``infile`` and write the answer to ``outfile``.

    This signature enables deterministic unit testing while still working with
    Judge0 (which provides stdin/stdout). Replace the body with the final
    algorithm for the problem, including any necessary parsing.
    """

    line = infile.read().strip()
    if not line:
        return

    limit = int(line)
    
    solution = Solution()
    result = solution.find_emirps_in_range(limit)
    
    if result:
        outfile.write(' '.join(map(str, result)) + '\n')
    else:
        outfile.write('\n')


if __name__ == "__main__":
    solve()