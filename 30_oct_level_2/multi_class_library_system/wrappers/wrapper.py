import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def execute_solution():
    try:
        commands = []
        for line in sys.stdin:
            line = line.strip()
            if line == "EXIT":
                break
            commands.append(line)
        
        solution = Solution()
        results = solution.processCommands(commands)
        
        for result in results:
            print(result)
        
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_solution()
