# wrapper.py - Execution wrapper for Judge0
# This file handles I/O and executes the contestant's Solution class

import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# Example of what gets injected:
# class Solution:
#     def methodName(self, param):
#         return result
# ===== END INJECTION POINT =====

def execute_solution():
    """
    Wrapper function to handle I/O and execute the contestant's solution
    """
    try:
        # Read input according to problem specification
        year = int(input().strip())
        
        # Create solution instance
        solution = Solution()
        
        # Call the solution method
        result = solution.isLeapYear(year)
        
        # Print output according to problem specification
        print("True" if result else "False")
        
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()