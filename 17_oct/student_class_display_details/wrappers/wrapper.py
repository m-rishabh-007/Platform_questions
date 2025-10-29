import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        parts = input().strip().split()
        if len(parts) != 3:
            print("Input must contain exactly 3 values.", file=sys.stderr)
            sys.exit(1)
        name = parts[0]
        roll = int(parts[1])
        marks = float(parts[2])
        solution = Solution()
        result = solution.getStudentDetails(name, roll, marks)
        print(result)
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
