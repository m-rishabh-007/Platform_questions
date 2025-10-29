import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n = int(input())
        intervals = []
        for _ in range(n):
            start, end = map(int, input().split())
            intervals.append([start, end])
        
        solution = Solution()
        result = solution.merge(intervals)
        
        for interval in result:
            print(interval[0], interval[1])
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
