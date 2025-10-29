from typing import TextIO, List
import sys

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        def dfs(i, j):
            # Base cases
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            # Mark as visited
            grid[i][j] = '0'
            
            # Visit all 4 adjacent cells
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    m, n = map(int, infile.readline().split())
    grid = []
    for _ in range(m):
        row = list(infile.readline().strip())
        grid.append(row)
    
    solution = Solution()
    result = solution.numIslands(grid)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
