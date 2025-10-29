class Solution(object):
    def maxProduct(self, nums, k, limit):
        """
        :type nums: List[int]
        :type k: int
        :type limit: int
        :rtype: int
        """
        from functools import lru_cache
        
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def dp(idx, current_sum, length):
            # Base case
            if idx == n:
                if current_sum == k and length > 0:
                    return 1
                return -1
            
            # Skip current element
            result = dp(idx + 1, current_sum, length)
            
            # Take current element
            sign = 1 if length % 2 == 0 else -1
            new_sum = current_sum + sign * nums[idx]
            sub_result = dp(idx + 1, new_sum, length + 1)
            
            if sub_result != -1:
                product = sub_result * nums[idx]
                if product <= limit:
                    result = max(result, product)
            
            return result
        
        return dp(0, 0, 0)

def solve(infile, outfile):
    """Standalone execution for orchestrator"""
    n, k, limit = map(int, infile.readline().split())
    nums = list(map(int, infile.readline().split()))
    
    solution = Solution()
    result = solution.maxProduct(nums, k, limit)
    outfile.write(str(result) + '\n')

if __name__ == "__main__":
    import sys
    solve(sys.stdin, sys.stdout)

