from typing import TextIO
import sys

class Solution:
    def findLargestOfThree(self, a: int, b: int, c: int) -> int:
        """
        Returns the largest of three integers using if-else logic.
        """
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    a, b, c = map(int, infile.read().strip().split())
    solution = Solution()
    result = solution.findLargestOfThree(a, b, c)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
