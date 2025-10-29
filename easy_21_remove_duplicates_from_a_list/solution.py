"""Reference implementation for the platform's official solution.

Update this file with the fully working algorithm that matches the
`description.txt` contract and is compatible with the wrappers.
"""

from __future__ import annotations

import sys
from typing import TextIO


class Solution:
    def removeDuplicates(self, numbers):
        """
        :type numbers: List[int]
        :rtype: List[int]
        """
        seen = set()
        result = []
        for num in numbers:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result


def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """Read from ``infile`` and write the answer to ``outfile``.

    This signature enables deterministic unit testing while still working with
    Judge0 (which provides stdin/stdout). Replace the body with the final
    algorithm for the problem, including any necessary parsing.
    """

    lines = infile.read().strip().split('\n')
    n = int(lines[0])
    numbers = list(map(int, lines[1].split()))
    
    # Create solution instance and call the method
    solution = Solution()
    result = solution.removeDuplicates(numbers)
    
    # Output the result
    outfile.write(' '.join(map(str, result)) + '\n')


if __name__ == "__main__":
    solve()
