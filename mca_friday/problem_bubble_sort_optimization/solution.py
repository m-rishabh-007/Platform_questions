from typing import TextIO
import sys

class Solution:
    def calculate_comparison_savings(self, arr):
        """
        Calculate the number of comparisons saved by optimized Bubble Sort.
        
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) <= 1:
            return 0
        
        def naive_bubble_sort(arr):
            arr = arr[:]
            n = len(arr)
            comparisons = 0
            
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    comparisons += 1
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            return comparisons
        
        def optimized_bubble_sort(arr):
            arr = arr[:]
            n = len(arr)
            comparisons = 0
            last_swap_index = n - 1
            
            while last_swap_index > 0:
                new_last_swap_index = 0
                
                for j in range(last_swap_index):
                    comparisons += 1
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        new_last_swap_index = j
                
                last_swap_index = new_last_swap_index
            
            return comparisons
        
        naive_comparisons = naive_bubble_sort(arr)
        optimized_comparisons = optimized_bubble_sort(arr)
        
        return naive_comparisons - optimized_comparisons

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n = int(infile.readline().strip())
    arr = list(map(int, infile.readline().strip().split()))
    
    solution = Solution()
    result = solution.calculate_comparison_savings(arr)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
