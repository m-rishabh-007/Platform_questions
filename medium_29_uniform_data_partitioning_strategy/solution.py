"""Reference implementation for the platform's official solution.

Update this file with the fully working algorithm that matches the
`description.txt` contract and is compatible with the wrappers.
"""

from __future__ import annotations

import sys
from typing import TextIO
import math


class Solution:
    def calculate_partition_plan(self, data_volumes):
        """
        :type data_volumes: List[int]
        :rtype: List[int]
        """
        if not data_volumes:
            return [0, 0]
        
        # Calculate GCD of all volumes
        partition_size = data_volumes[0]
        for volume in data_volumes[1:]:
            partition_size = math.gcd(partition_size, volume)
        
        # Calculate total partitions needed
        total_partitions = sum(volume // partition_size for volume in data_volumes)
        
        return [partition_size, total_partitions]


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
    data_volumes = list(map(int, lines[1].split()))
    
    solution = Solution()
    result = solution.calculate_partition_plan(data_volumes)
    
    outfile.write(f"{result[0]} {result[1]}\n")


if __name__ == "__main__":
    solve()