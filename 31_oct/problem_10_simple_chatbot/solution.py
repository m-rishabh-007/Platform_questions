class Solution(object):
    def chatbotResponses(self, messages):
        """
        :type messages: List[str]
        :rtype: List[str]
        """
        responses = []
        
        for msg in messages:
            msg_lower = msg.lower()
            msg_words = set(msg_lower.split())
            
            # Check for greetings (as separate words or at start)
            if any(word in msg_words for word in ["hello", "hi", "hey"]) or msg_lower.startswith("hello") or msg_lower.startswith("hi") or msg_lower.startswith("hey"):
                responses.append("Hi there! How can I help you?")
            # Check for farewells
            elif any(word in msg_words for word in ["bye", "goodbye", "exit"]) or "bye" in msg_lower:
                responses.append("Goodbye! Have a great day!")
            # Check for weather keywords
            elif any(keyword in msg_lower for keyword in ["weather", "temperature", "forecast"]):
                responses.append("I'm sorry, I can't check the weather, but it's always nice to go outside!")
            # Check for name/identity
            elif "name" in msg_lower or "who are you" in msg_lower:
                responses.append("I'm a simple chatbot created to assist you.")
            # Check for help keywords
            elif any(keyword in msg_lower for keyword in ["help", "assist", "support"]):
                responses.append("I can chat with you! Try asking about the weather or saying hello.")
            else:
                responses.append("I'm not sure I understand. Can you rephrase that?")
        
        return responses

def solve(infile, outfile):
    """Standalone execution for orchestrator"""
    n = int(infile.readline())
    messages = []
    for _ in range(n):
        messages.append(infile.readline().strip())
    
    solution = Solution()
    responses = solution.chatbotResponses(messages)
    
    for response in responses:
        outfile.write(response + '\n')

if __name__ == "__main__":
    import sys
    solve(sys.stdin, sys.stdout)

