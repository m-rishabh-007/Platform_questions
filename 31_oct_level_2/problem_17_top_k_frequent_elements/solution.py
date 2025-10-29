from typing import TextIO, List
import sys

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        
        # Count frequencies
        freq = Counter(nums)
        
        # Use heap to get top k
        # Python's heapq is min heap, so negate frequencies for max heap behavior
        result = heapq.nlargest(k, freq.keys(), key=freq.get)
        
        # Sort result for consistent output
        result.sort()
        return result

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n, k = map(int, infile.readline().split())
    nums = list(map(int, infile.readline().split()))
    
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    
    outfile.write(' '.join(map(str, result)) + '\n')

if __name__ == "__main__":
    solve()
