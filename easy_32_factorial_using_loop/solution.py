from typing import TextIO
import sys

class Solution:
    def computeFactorial(self, n: int) -> int:
        """
        Returns the factorial of n using a loop.
        """
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n = int(infile.read().strip())
    solution = Solution()
    result = solution.computeFactorial(n)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
