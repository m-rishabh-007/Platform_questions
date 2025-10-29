from typing import TextIO
import sys

class Solution:
    def sumOfFive(self, arr):
        """
        Returns the sum of an array of 5 integers.
        """
        return sum(arr)

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    arr = list(map(int, infile.read().strip().split()))
    solution = Solution()
    result = solution.sumOfFive(arr)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
