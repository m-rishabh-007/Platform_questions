from typing import TextIO
import sys

class Solution:
    def sum_of_prime_factors(self, n):
        """
        Calculate the sum of distinct prime factors of n.
        
        :type n: int
        :rtype: int
        """
        sum_factors = 0
        
        # Check for factor 2
        if n % 2 == 0:
            sum_factors += 2
            while n % 2 == 0:
                n //= 2
        
        # Check for odd factors from 3 onwards
        i = 3
        while i * i <= n:
            if n % i == 0:
                sum_factors += i
                while n % i == 0:
                    n //= i
            i += 2
        
        # If n is still greater than 1, then it's a prime factor
        if n > 1:
            sum_factors += n
        
        return sum_factors

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n = int(infile.read().strip())
    
    solution = Solution()
    result = solution.sum_of_prime_factors(n)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
