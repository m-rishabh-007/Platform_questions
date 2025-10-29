import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        t = int(input())
        solution = Solution()
        
        for _ in range(t):
            n, m, h = map(int, input().split())
            capacity = list(map(int, input().split()))
            power = list(map(int, input().split()))
            
            result = solution.maxEnergy(n, m, h, capacity, power)
            print(result)
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
