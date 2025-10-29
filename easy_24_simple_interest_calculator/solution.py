"""Reference implementation for the platform's official solution."""

from __future__ import annotations
import sys
from typing import TextIO

class Solution:
    def calculateSimpleInterest(self, principal, rate, time):
        """
        :type principal: float
        :type rate: float
        :type time: float
        :rtype: float
        """
        return (principal * rate * time) / 100

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    line = infile.read().strip()
    principal, rate, time = map(float, line.split())
    
    solution = Solution()
    result = solution.calculateSimpleInterest(principal, rate, time)
    
    outfile.write(f"{result:.2f}\n")

if __name__ == "__main__":
    solve()
