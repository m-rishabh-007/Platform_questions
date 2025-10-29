from typing import TextIO
import sys

class Solution:
    def swapNumbers(self, a: int, b: int) -> tuple:
        """
        Returns the swapped values of a and b as a tuple.
        """
        return (b, a)

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    a, b = map(int, infile.read().strip().split())
    solution = Solution()
    swapped = solution.swapNumbers(a, b)
    outfile.write(f"{swapped[0]} {swapped[1]}\n")

if __name__ == "__main__":
    solve()
