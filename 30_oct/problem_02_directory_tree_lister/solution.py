from typing import TextIO
import sys
import json

class Solution:
    def listDirectoryTree(self, fs):
        self._print_recursive(fs, 0)
    
    def _print_recursive(self, node, depth):
        sorted_keys = sorted(node.keys())
        
        for key in sorted_keys:
            print('  ' * depth + key, end='')
            
            value = node[key]
            if isinstance(value, dict):
                print('/')
                self._print_recursive(value, depth + 1)
            else:
                print()

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    fs_json = infile.readline().strip()
    fs = json.loads(fs_json)
    
    solution = Solution()
    solution.listDirectoryTree(fs)

if __name__ == "__main__":
    solve()
