import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        a, b = map(int, input().strip().split())
        solution = Solution()
        swapped = solution.swapNumbers(a, b)
        print(f"{swapped[0]} {swapped[1]}")
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
