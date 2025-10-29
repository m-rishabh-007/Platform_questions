from typing import TextIO
import sys

class Solution:
    def areBracketsBalanced(self, s):
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    s = infile.readline().strip()
    
    solution = Solution()
    result = solution.areBracketsBalanced(s)
    
    outfile.write("true\n" if result else "false\n")

if __name__ == "__main__":
    solve()
