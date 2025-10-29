from typing import TextIO
import sys

class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        result = []
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1

        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
                
        return result

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    m, n = map(int, infile.readline().split())
    matrix = []
    for _ in range(m):
        row = list(map(int, infile.readline().split()))
        matrix.append(row)
    
    solution = Solution()
    result = solution.spiralOrder(matrix)
    
    outfile.write(' '.join(map(str, result)) + '\n')

if __name__ == "__main__":
    solve()
