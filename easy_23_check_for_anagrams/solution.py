"""Reference implementation for the platform's official solution.

Update this file with the fully working algorithm that matches the
`description.txt` contract and is compatible with the wrappers.
"""

from __future__ import annotations

import sys
from typing import TextIO


class Solution:
    def isAnagram(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        # Clean strings: remove spaces and convert to lowercase
        clean_str1 = ''.join(str1.lower().split())
        clean_str2 = ''.join(str2.lower().split())
        
        # Check if sorted characters are equal
        return sorted(clean_str1) == sorted(clean_str2)


def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """Read from ``infile`` and write the answer to ``outfile``.

    This signature enables deterministic unit testing while still working with
    Judge0 (which provides stdin/stdout). Replace the body with the final
    algorithm for the problem, including any necessary parsing.
    """

    lines = infile.read().strip().split('\n')
    str1 = lines[0]
    str2 = lines[1]
    
    # Create solution instance and call the method
    solution = Solution()
    result = solution.isAnagram(str1, str2)
    
    # Output the result
    outfile.write(f"{'True' if result else 'False'}\n")


if __name__ == "__main__":
    solve()
