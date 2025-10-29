import sys
from typing import TextIO

class Solution(object):
    def lowestCommonAncestor(self, tree_data, p, q):
        """
        :type tree_data: List[List[int]]  # [[node_id, parent_id, value], ...]
        :type p: int
        :type q: int
        :rtype: int
        """
        # Build tree structure and find p, q nodes
        value_to_id = {}
        id_to_parent = {}
        id_to_value = {}
        
        for node_id, parent_id, value in tree_data:
            value_to_id[value] = node_id
            id_to_parent[node_id] = parent_id
            id_to_value[node_id] = value
        
        # Get node IDs for p and q
        p_id = value_to_id[p]
        q_id = value_to_id[q]
        
        # Get ancestors of p
        p_ancestors = set()
        current = p_id
        while current != -1:
            p_ancestors.add(current)
            current = id_to_parent.get(current, -1)
        
        # Find first common ancestor starting from q
        current = q_id
        while current != -1:
            if current in p_ancestors:
                return id_to_value[current]
            current = id_to_parent.get(current, -1)
        
        return -1  # Should never reach here if p,q exist

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """For orchestrator.py execution"""
    n = int(infile.readline())
    tree_data = []
    for _ in range(n):
        parts = list(map(int, infile.readline().split()))
        tree_data.append(parts)
    
    p, q = map(int, infile.readline().split())
    
    solution = Solution()
    result = solution.lowestCommonAncestor(tree_data, p, q)
    outfile.write(str(result) + '\n')

if __name__ == "__main__":
    solve()
