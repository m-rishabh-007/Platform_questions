"""Reference implementation for the platform's official solution.

Update this file with the fully working algorithm that matches the
`description.txt` contract and is compatible with the wrappers.
"""

from __future__ import annotations

import sys
from typing import TextIO


class Solution:
    def analyze_sort_performance(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        if n <= 1:
            return [0, 0]
        
        # Calculate naive bubble sort metrics
        naive_comparisons = sum(n - 1 - i for i in range(n - 1))
        naive_swaps = self._count_naive_swaps(arr[:])
        
        # Calculate optimized bubble sort metrics
        optimized_comparisons, optimized_swaps = self._count_optimized_metrics(arr[:])
        
        comparison_savings = naive_comparisons - optimized_comparisons
        swap_savings = naive_swaps - optimized_swaps
        
        return [comparison_savings, swap_savings]
    
    def _count_naive_swaps(self, arr):
        """Count swaps in naive bubble sort"""
        n = len(arr)
        swap_count = 0
        
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap_count += 1
        
        return swap_count
    
    def _count_optimized_metrics(self, arr):
        """Count comparisons and swaps in optimized bubble sort"""
        n = len(arr)
        comparison_count = 0
        swap_count = 0
        boundary = n - 1
        
        while boundary > 0:
            last_swap_index = -1
            current_comparisons = 0
            current_swaps = 0
            
            # Perform comparisons up to the boundary
            for j in range(boundary):
                current_comparisons += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    current_swaps += 1
                    last_swap_index = j
            
            comparison_count += current_comparisons
            swap_count += current_swaps
            
            # Early termination if no swaps occurred
            if current_swaps == 0:
                break
                
            # Update boundary to last swap position
            boundary = last_swap_index
        
        return comparison_count, swap_count


def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """Read from ``infile`` and write the answer to ``outfile``.

    This signature enables deterministic unit testing while still working with
    Judge0 (which provides stdin/stdout). Replace the body with the final
    algorithm for the problem, including any necessary parsing.
    """

    lines = infile.read().strip().split('\n')
    if len(lines) < 2:
        return

    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    
    solution = Solution()
    result = solution.analyze_sort_performance(arr)
    
    outfile.write(f"{result[0]} {result[1]}\n")


if __name__ == "__main__":
    solve()