import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        arr = list(map(int, input().strip().split()))
        if len(arr) != 5:
            print("Input must contain exactly 5 integers.", file=sys.stderr)
            sys.exit(1)
        solution = Solution()
        result = solution.sumOfFive(arr)
        print(result)
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
