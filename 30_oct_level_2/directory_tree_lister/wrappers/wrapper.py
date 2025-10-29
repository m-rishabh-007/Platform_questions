import sys
import json

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        fs_json = input().strip()
        fs = json.loads(fs_json)
        
        solution = Solution()
        solution.listDirectoryTree(fs)
        
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
