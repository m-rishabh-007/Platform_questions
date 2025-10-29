"""Reference implementation for the platform's official solution."""

from __future__ import annotations
import sys
from typing import TextIO

class Solution:
    def isLeapYear(self, year):
        """
        :type year: int
        :rtype: bool
        """
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    year = int(infile.read().strip())
    
    solution = Solution()
    result = solution.isLeapYear(year)
    
    outfile.write(f"{'True' if result else 'False'}\n")

if __name__ == "__main__":
    solve()
