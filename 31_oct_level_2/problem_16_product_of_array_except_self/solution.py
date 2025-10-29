from typing import TextIO, List
import sys

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        
        # First pass: calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Second pass: calculate suffix products and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n = int(infile.readline())
    nums = list(map(int, infile.readline().split()))
    
    solution = Solution()
    result = solution.productExceptSelf(nums)
    
    outfile.write(' '.join(map(str, result)) + '\n')

if __name__ == "__main__":
    solve()
