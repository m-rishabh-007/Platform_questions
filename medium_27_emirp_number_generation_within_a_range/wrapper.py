# wrapper.py - Execution wrapper for Judge0
# This file handles I/O and executes the contestant's Solution class

import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# Example of what gets injected:
# class Solution:
#     def find_emirps_in_range(self, limit):
#         return []
# ===== END INJECTION POINT =====

def execute_solution():
    """
    Wrapper function to handle I/O and execute the contestant's solution
    """
    try:
        # Read input according to problem specification
        limit = int(input().strip())
        
        # Create solution instance
        solution = Solution()
        
        # Call the solution method
        result = solution.find_emirps_in_range(limit)
        
        # Print output according to problem specification
        if result:
            print(' '.join(map(str, result)))
        else:
            print()
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()