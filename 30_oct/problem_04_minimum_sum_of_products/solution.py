from typing import TextIO
import sys

class Solution:
    def minSumOfProducts(self, A, B):
        A.sort()
        B.sort()
        
        n = len(B)
        A_sub = A[:n]
        
        min_sum = 0
        for i in range(n):
            min_sum += A_sub[i] * B[n - 1 - i]
            
        return min_sum

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    A = list(map(int, infile.readline().split()))
    B = list(map(int, infile.readline().split()))
    
    solution = Solution()
    result = solution.minSumOfProducts(A, B)
    
    outfile.write(str(result) + '\n')

if __name__ == "__main__":
    solve()
