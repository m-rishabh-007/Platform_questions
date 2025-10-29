from typing import TextIO, List
import sys

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # If current interval overlaps with the last merged interval
            if intervals[i][0] <= merged[-1][1]:
                # Merge by updating the end time
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                # No overlap, add as new interval
                merged.append(intervals[i])
        
        return merged

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n = int(infile.readline())
    intervals = []
    for _ in range(n):
        start, end = map(int, infile.readline().split())
        intervals.append([start, end])
    
    solution = Solution()
    result = solution.merge(intervals)
    
    for interval in result:
        outfile.write(f"{interval[0]} {interval[1]}\n")

if __name__ == "__main__":
    solve()
