import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        a, b, c = map(int, input().strip().split())
        solution = Solution()
        result = solution.findLargestOfThree(a, b, c)
        print(result)
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
