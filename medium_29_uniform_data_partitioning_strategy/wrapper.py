# wrapper.py - Execution wrapper for Judge0
# This file handles I/O and executes the contestant's Solution class

import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# Example of what gets injected:
# class Solution:
#     def calculate_partition_plan(self, data_volumes):
#         return [0, 0]
# ===== END INJECTION POINT =====

def execute_solution():
    """
    Wrapper function to handle I/O and execute the contestant's solution
    """
    try:
        # Read input according to problem specification
        n = int(input().strip())
        data_volumes = list(map(int, input().strip().split()))
        
        # Create solution instance
        solution = Solution()
        
        # Call the solution method
        result = solution.calculate_partition_plan(data_volumes)
        
        # Print output according to problem specification
        print(f"{result[0]} {result[1]}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()