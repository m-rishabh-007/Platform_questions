import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n = int(input())
        messages = []
        for _ in range(n):
            messages.append(input())
        
        solution = Solution()
        responses = solution.chatbotResponses(messages)
        
        for response in responses:
            print(response)
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
