import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        
        solution = Solution()
        result = solution.topKFrequent(nums, k)
        
        print(' '.join(map(str, result)))
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
