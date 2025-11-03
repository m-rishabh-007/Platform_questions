from typing import TextIO
import sys

class Solution:
    def total_branches(self, n):
        """
        Calculate total branches up to level n following Tribonacci pattern.
        
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 4
        
        # Calculate Tribonacci values (new branches at each level)
        trib0, trib1, trib2 = 1, 1, 2
        total = 1 + 1 + 2  # Sum of first 3 levels
        
        for i in range(3, n + 1):
            new_branches = trib0 + trib1 + trib2
            total += new_branches
            
            trib0 = trib1
            trib1 = trib2
            trib2 = new_branches
        
        return total

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n = int(infile.read().strip())
    
    solution = Solution()
    result = solution.total_branches(n)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
