from typing import TextIO
import sys

class Solution:
    def processCommands(self, commands):
        """
        :type commands: List[str]
        :rtype: List[str]
        """
        books = {}
        members = {}
        results = []
        
        for cmd in commands:
            parts = self._parse_command(cmd)
            
            if parts[0] == "ADD" and parts[1] == "BOOK":
                title, author = parts[2], parts[3]
                if title not in books:
                    books[title] = {'author': author, 'checked_out': False, 'by': None}
                    results.append(f'Book "{title}" added.')
                    
            elif parts[0] == "ADD" and parts[1] == "MEMBER":
                name, member_id = parts[2], int(parts[3])
                if member_id not in members:
                    members[member_id] = name
                    results.append(f'Member "{name}" registered.')
                    
            elif parts[0] == "CHECKOUT":
                member_id = int(parts[1])
                title = parts[2]
                
                if member_id not in members:
                    results.append("Error: Member not found.")
                elif title not in books:
                    results.append("Error: Book not found.")
                elif books[title]['checked_out']:
                    results.append("Error: Book not available.")
                else:
                    books[title]['checked_out'] = True
                    books[title]['by'] = member_id
                    results.append("Checkout successful.")
                    
            elif parts[0] == "RETURN":
                title = parts[1]
                if title not in books or not books[title]['checked_out']:
                    results.append("Error: Book not in records or was not checked out.")
                else:
                    books[title]['checked_out'] = False
                    books[title]['by'] = None
                    results.append("Return successful.")
        
        return results
    
    def _parse_command(self, cmd):
        parts = []
        in_quote = False
        current = ""
        
        for char in cmd:
            if char == '"':
                in_quote = not in_quote
            elif char == ' ' and not in_quote:
                if current:
                    parts.append(current)
                    current = ""
            else:
                current += char
        
        if current:
            parts.append(current)
        
        return parts

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    commands = []
    for line in infile:
        line = line.strip()
        if line == "EXIT":
            break
        commands.append(line)
    
    solution = Solution()
    results = solution.processCommands(commands)
    
    for result in results:
        outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
