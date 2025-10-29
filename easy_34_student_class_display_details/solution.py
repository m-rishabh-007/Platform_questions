from typing import TextIO
import sys

class Solution:
    def getStudentDetails(self, name: str, roll: int, marks: float) -> str:
        """
        Returns a formatted string with student details.
        """
        return f"Name: {name}, Roll: {roll}, Marks: {marks}"

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    parts = infile.read().strip().split()
    name = parts[0]
    roll = int(parts[1])
    marks = float(parts[2])
    solution = Solution()
    result = solution.getStudentDetails(name, roll, marks)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
