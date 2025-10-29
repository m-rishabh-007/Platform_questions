import sys
from typing import TextIO

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        components = 0
        
        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        
        return components

def solve(infile=None, outfile=None):
    """Standalone execution for orchestrator"""
    if infile is None:
        infile = sys.stdin
    if outfile is None:
        outfile = sys.stdout
    
    n, m = map(int, infile.readline().split())
    edges = []
    for _ in range(m):
        line = infile.readline().strip()
        if line:  # Only process non-empty lines
            u, v = map(int, line.split())
            edges.append([u, v])
    
    solution = Solution()
    result = solution.countComponents(n, edges)
    outfile.write(str(result) + '\n')

if __name__ == "__main__":
    solve()
