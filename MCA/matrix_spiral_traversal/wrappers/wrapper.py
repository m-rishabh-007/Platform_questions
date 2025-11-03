import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        m, n = map(int, input().strip().split())
        matrix = []
        for _ in range(m):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        
        solution = Solution()
        result = solution.spiralOrder(matrix)
        
        print(' '.join(map(str, result)))
        
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
