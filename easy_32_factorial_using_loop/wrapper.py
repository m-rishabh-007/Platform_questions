import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        n = int(input().strip())
        solution = Solution()
        result = solution.computeFactorial(n)
        print(result)
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
