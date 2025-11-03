import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        
        solution = Solution()
        result = solution.minSumOfProducts(A, B)
        
        print(result)
        
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
