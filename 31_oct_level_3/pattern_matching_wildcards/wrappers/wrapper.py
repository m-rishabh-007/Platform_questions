import sys

# ===== PLATFORM INJECTION POINT =====
# The platform will inject the contestant's Solution class here.
# It must define:
#   class Solution(object):
#       def isMatch(self, s, p):
#           ...
# ===== END PLATFORM INJECTION POINT =====

def main():
    try:
        # Read input
        s = sys.stdin.readline().strip()
        p = sys.stdin.readline().strip()
        
        # Create solution instance and call method
        solution = Solution()
        result = solution.isMatch(s, p)
        
        # Output result
        print("true" if result else "false")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
