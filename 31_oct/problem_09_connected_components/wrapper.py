import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n, m = map(int, input().split())
        edges = []
        for _ in range(m):
            u, v = map(int, input().split())
            edges.append([u, v])
        
        solution = Solution()
        result = solution.countComponents(n, edges)
        print(result)
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
