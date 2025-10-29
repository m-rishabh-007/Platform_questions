import sys
from typing import List

# ===== PLATFORM INJECTION POINT =====
# The platform will inject the contestant's Solution class here.
# It must define:
#   class Solution(object):
#       def lengthOfLIS(self, nums, k):
#           ...
# ===== END PLATFORM INJECTION POINT =====

def main():
    try:
        # Read input
        n, k = map(int, sys.stdin.readline().split())
        nums = list(map(int, sys.stdin.readline().split()))
        
        # Create solution instance and call method
        solution = Solution()
        result = solution.lengthOfLIS(nums, k)
        
        # Output result
        print(result)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
