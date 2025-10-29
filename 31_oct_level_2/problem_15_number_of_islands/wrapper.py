import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        m, n = map(int, input().split())
        grid = []
        for _ in range(m):
            row = list(input().strip())
            grid.append(row)
        
        solution = Solution()
        result = solution.numIslands(grid)
        print(result)
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
