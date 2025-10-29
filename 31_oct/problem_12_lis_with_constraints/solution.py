import sys
from typing import List

class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        # dp[i] = length of longest increasing subsequence ending at index i
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] > nums[j] and difference constraint satisfied
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

def solve(infile, outfile):
    """Standalone execution for orchestrator"""
    n, k = map(int, infile.readline().split())
    nums = list(map(int, infile.readline().split()))
    
    solution = Solution()
    result = solution.lengthOfLIS(nums, k)
    outfile.write(str(result) + '\n')

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
