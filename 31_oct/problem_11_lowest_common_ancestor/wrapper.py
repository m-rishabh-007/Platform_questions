import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n = int(input())
        tree_data = []
        for _ in range(n):
            parts = list(map(int, input().split()))
            tree_data.append(parts)
        
        p, q = map(int, input().split())
        
        solution = Solution()
        result = solution.lowestCommonAncestor(tree_data, p, q)
        print(result)
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
