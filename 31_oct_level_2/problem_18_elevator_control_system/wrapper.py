import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n, m, t = map(int, input().split())
        requests = []
        for _ in range(t):
            requests.append(input().strip())
        
        solution = Solution()
        output = solution.simulateElevatorSystem(n, m, requests)
        
        for line in output:
            print(line)
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
