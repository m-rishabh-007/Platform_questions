import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        line = input().split()
        n = int(line[0])
        k = int(line[1])
        limit = int(line[2])
        
        nums = list(map(int, input().split()))
        
        solution = Solution()
        result = solution.maxProduct(nums, k, limit)
        print(result)
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
