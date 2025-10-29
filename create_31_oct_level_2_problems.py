#!/usr/bin/env python3
"""
Generator script for 31_oct_level_2 problems
Creates 5 problems based on problems.txt and problems_details.txt
Following 30_oct/ canonical format with all 10 required files per problem
"""

import os
import json

# Base directory
BASE_DIR = "31_oct_level_2"

# Problem 1: Merge Overlapping Intervals
problem_14_files = {
    "description.txt": """Merge Overlapping Intervals

You are given an array of intervals where intervals[i] = [start_i, end_i].
Merge all overlapping intervals and return an array of non-overlapping intervals.

## Input Format
- First line: Integer n (number of intervals)
- Next n lines: Two integers (start, end) for each interval

## Output Format
- Print merged intervals, one per line (start end)

## Constraints
- 1 ≤ n ≤ 10^4
- 0 ≤ start_i < end_i ≤ 10^4

## Sample Input 1
```
4
1 3
2 6
8 10
15 18
```

## Sample Output 1
```
1 6
8 10
15 18
```

## Sample Input 2
```
2
1 4
4 5
```

## Sample Output 2
```
1 5
```

## Sample Input 3
```
3
1 2
3 4
5 6
```

## Sample Output 3
```
1 2
3 4
5 6
```

## Sample Input 4
```
1
1 10
```

## Sample Output 4
```
1 10
```
""",

    "template.py": """class Solution(object):
    def merge(self, intervals):
        \"\"\"
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        \"\"\"
        return []
""",

    "template.cpp": """class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals);
};
""",

    "solution.py": """from typing import TextIO, List
import sys

class Solution(object):
    def merge(self, intervals):
        \"\"\"
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        \"\"\"
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
        outfile.write(f"{interval[0]} {interval[1]}\\n")

if __name__ == "__main__":
    solve()
""",

    "solution.cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        
        // Sort intervals by start time
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> merged;
        merged.push_back(intervals[0]);
        
        for (int i = 1; i < intervals.size(); i++) {
            // If current interval overlaps with the last merged interval
            if (intervals[i][0] <= merged.back()[1]) {
                // Merge by updating the end time
                merged.back()[1] = max(merged.back()[1], intervals[i][1]);
            } else {
                // No overlap, add as new interval
                merged.push_back(intervals[i]);
            }
        }
        
        return merged;
    }
};

void solve() {
    int n;
    cin >> n;
    
    vector<vector<int>> intervals(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> intervals[i][0] >> intervals[i][1];
    }
    
    Solution solution;
    vector<vector<int>> result = solution.merge(intervals);
    
    for (const auto& interval : result) {
        cout << interval[0] << " " << interval[1] << endl;
    }
}

int main() {
    solve();
    return 0;
}
""",

    "wrapper.py": """import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n = int(input())
        intervals = []
        for _ in range(n):
            start, end = map(int, input().split())
            intervals.append([start, end])
        
        solution = Solution()
        result = solution.merge(intervals)
        
        for interval in result:
            print(interval[0], interval[1])
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
""",

    "wrapper.cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int n;
    cin >> n;
    
    vector<vector<int>> intervals(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> intervals[i][0] >> intervals[i][1];
    }
    
    Solution solution;
    vector<vector<int>> result = solution.merge(intervals);
    
    for (const auto& interval : result) {
        cout << interval[0] << " " << interval[1] << endl;
    }
    
    return 0;
}
""",

    "generator.py": """import random
import json
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            [(1, 1)],  # Single interval
            [(1, 2), (3, 4)],  # No overlap
            [(1, 5), (2, 3)],  # Nested
            [(1, 3), (2, 4), (3, 5)],  # Chain overlap
            [(1, 10)],  # Single large interval
        ]
        intervals = rng.choice(edge_types)
        
    elif rule_type == "small":
        n = rng.randint(1, 5)
        intervals = []
        for _ in range(n):
            start = rng.randint(0, 50)
            end = rng.randint(start + 1, start + 20)
            intervals.append((start, end))
    
    elif rule_type == "medium":
        n = rng.randint(5, 50)
        intervals = []
        for _ in range(n):
            start = rng.randint(0, 500)
            end = rng.randint(start + 1, start + 100)
            intervals.append((start, end))
    
    elif rule_type == "large":
        n = rng.randint(50, 1000)
        intervals = []
        for _ in range(n):
            start = rng.randint(0, 5000)
            end = rng.randint(start + 1, start + 200)
            intervals.append((start, end))
    
    elif rule_type == "stress":
        n = rng.randint(1000, 10000)
        intervals = []
        for _ in range(n):
            start = rng.randint(0, 10000)
            end = rng.randint(start + 1, min(start + 500, 10000))
            intervals.append((start, end))
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Format output
    output = f"{len(intervals)}\\n"
    for start, end in intervals:
        output += f"{start} {end}\\n"
    
    return output

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate test cases')
    parser.add_argument('rule_type', type=str, help='Type of test case to generate')
    parser.add_argument('--args', type=str, default='{}', help='Arguments as JSON string')
    parser.add_argument('--rng-seed', type=int, help='Random seed')
    
    args = parser.parse_args()
    
    test_args = json.loads(args.args)
    if args.rng_seed is not None:
        test_args['seed'] = args.rng_seed
    
    result = generate_case(args.rule_type, test_args)
    print(result, end='')
""",

    "config.json": json.dumps({
        "generation_logic": [
            {"type": "edge_cases", "count": 5, "args": {}},
            {"type": "small", "count": 10, "args": {}},
            {"type": "medium", "count": 15, "args": {}},
            {"type": "large", "count": 15, "args": {}},
            {"type": "stress", "count": 10, "args": {}}
        ]
    }, indent=2),

    "examples.json": json.dumps([
        {
            "stdin": "4\\n1 3\\n2 6\\n8 10\\n15 18\\n",
            "expected_output": "1 6\\n8 10\\n15 18\\n",
            "visibility": "visible"
        },
        {
            "stdin": "2\\n1 4\\n4 5\\n",
            "expected_output": "1 5\\n",
            "visibility": "visible"
        },
        {
            "stdin": "3\\n1 2\\n3 4\\n5 6\\n",
            "expected_output": "1 2\\n3 4\\n5 6\\n",
            "visibility": "visible"
        },
        {
            "stdin": "1\\n1 10\\n",
            "expected_output": "1 10\\n",
            "visibility": "visible"
        }
    ], indent=2)
}

# Problem 2: Number of Islands
problem_15_files = {
    "description.txt": """Number of Islands

You are given an m × n 2D binary grid which represents a map of '1's (land) 
and '0's (water). An island is formed by connecting adjacent lands horizontally 
or vertically.

Count the total number of islands. Assume all four edges are surrounded by water.

## Input Format
- First line: Two integers m n (rows and columns)
- Next m lines: n characters ('0' or '1')

## Output Format
- Single integer: number of islands

## Constraints
- 1 ≤ m, n ≤ 300
- grid[i][j] is '0' or '1'

## Sample Input 1
```
4 5
11000
11000
00100
00011
```

## Sample Output 1
```
3
```

## Sample Input 2
```
3 3
111
010
111
```

## Sample Output 2
```
1
```

## Sample Input 3
```
2 2
10
01
```

## Sample Output 3
```
2
```

## Sample Input 4
```
1 1
0
```

## Sample Output 4
```
0
```
""",

    "template.py": """class Solution(object):
    def numIslands(self, grid):
        \"\"\"
        :type grid: List[List[str]]
        :rtype: int
        \"\"\"
        return 0
""",

    "template.cpp": """class Solution {
public:
    int numIslands(vector<vector<char>>& grid);
};
""",

    "solution.py": """from typing import TextIO, List
import sys

class Solution(object):
    def numIslands(self, grid):
        \"\"\"
        :type grid: List[List[str]]
        :rtype: int
        \"\"\"
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        def dfs(i, j):
            # Base cases
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            # Mark as visited
            grid[i][j] = '0'
            
            # Visit all 4 adjacent cells
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    m, n = map(int, infile.readline().split())
    grid = []
    for _ in range(m):
        row = list(infile.readline().strip())
        grid.append(row)
    
    solution = Solution()
    result = solution.numIslands(grid)
    outfile.write(f"{result}\\n")

if __name__ == "__main__":
    solve()
""",

    "solution.cpp": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
private:
    void dfs(vector<vector<char>>& grid, int i, int j) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Base cases
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') {
            return;
        }
        
        // Mark as visited
        grid[i][j] = '0';
        
        // Visit all 4 adjacent cells
        dfs(grid, i + 1, j);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i, j - 1);
    }
    
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        int count = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        
        return count;
    }
};

void solve() {
    int m, n;
    cin >> m >> n;
    
    vector<vector<char>> grid(m, vector<char>(n));
    for (int i = 0; i < m; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < n; j++) {
            grid[i][j] = row[j];
        }
    }
    
    Solution solution;
    cout << solution.numIslands(grid) << endl;
}

int main() {
    solve();
    return 0;
}
""",

    "wrapper.py": """import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        m, n = map(int, input().split())
        grid = []
        for _ in range(m):
            row = list(input().strip())
            grid.append(row)
        
        solution = Solution()
        result = solution.numIslands(grid)
        print(result)
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
""",

    "wrapper.cpp": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int m, n;
    cin >> m >> n;
    
    vector<vector<char>> grid(m, vector<char>(n));
    for (int i = 0; i < m; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < n; j++) {
            grid[i][j] = row[j];
        }
    }
    
    Solution solution;
    cout << solution.numIslands(grid) << endl;
    
    return 0;
}
""",

    "generator.py": """import random
import json
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            (1, 1, 0.0),  # Single water
            (1, 1, 1.0),  # Single land
            (2, 2, 0.5),  # Tiny grid
            (3, 3, 0.3),  # Small grid sparse
            (5, 5, 0.0),  # All water
        ]
        m, n, land_prob = rng.choice(edge_types)
    
    elif rule_type == "small":
        m = rng.randint(2, 10)
        n = rng.randint(2, 10)
        land_prob = rng.uniform(0.2, 0.8)
    
    elif rule_type == "medium":
        m = rng.randint(10, 50)
        n = rng.randint(10, 50)
        land_prob = rng.uniform(0.3, 0.7)
    
    elif rule_type == "large":
        m = rng.randint(50, 150)
        n = rng.randint(50, 150)
        land_prob = rng.uniform(0.3, 0.6)
    
    elif rule_type == "stress":
        m = rng.randint(150, 300)
        n = rng.randint(150, 300)
        land_prob = rng.uniform(0.3, 0.5)
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Generate grid
    grid = []
    for _ in range(m):
        row = ''.join('1' if rng.random() < land_prob else '0' for _ in range(n))
        grid.append(row)
    
    # Format output
    output = f"{m} {n}\\n"
    for row in grid:
        output += f"{row}\\n"
    
    return output

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate test cases')
    parser.add_argument('rule_type', type=str, help='Type of test case to generate')
    parser.add_argument('--args', type=str, default='{}', help='Arguments as JSON string')
    parser.add_argument('--rng-seed', type=int, help='Random seed')
    
    args = parser.parse_args()
    
    test_args = json.loads(args.args)
    if args.rng_seed is not None:
        test_args['seed'] = args.rng_seed
    
    result = generate_case(args.rule_type, test_args)
    print(result, end='')
""",

    "config.json": json.dumps({
        "generation_logic": [
            {"type": "edge_cases", "count": 5, "args": {}},
            {"type": "small", "count": 10, "args": {}},
            {"type": "medium", "count": 15, "args": {}},
            {"type": "large", "count": 15, "args": {}},
            {"type": "stress", "count": 10, "args": {}}
        ]
    }, indent=2),

    "examples.json": json.dumps([
        {
            "stdin": "4 5\\n11000\\n11000\\n00100\\n00011\\n",
            "expected_output": "3\\n",
            "visibility": "visible"
        },
        {
            "stdin": "3 3\\n111\\n010\\n111\\n",
            "expected_output": "1\\n",
            "visibility": "visible"
        },
        {
            "stdin": "2 2\\n10\\n01\\n",
            "expected_output": "2\\n",
            "visibility": "visible"
        },
        {
            "stdin": "1 1\\n0\\n",
            "expected_output": "0\\n",
            "visibility": "visible"
        }
    ], indent=2)
}

# Problem 3: Product of Array Except Self
problem_16_files = {
    "description.txt": """Product of Array Except Self

Given an integer array nums, return an answer array such that answer[i] is 
equal to the product of all elements of nums except nums[i].

## Input Format
- First line: Integer n (array length)
- Second line: n space-separated integers

## Output Format
- n space-separated integers (the answer array)

## Constraints
- 2 ≤ n ≤ 10^5
- -30 ≤ nums[i] ≤ 30
- Product of any prefix or suffix guaranteed to fit in 32-bit integer
- O(n) time complexity required
- Cannot use division operation

## Sample Input 1
```
4
1 2 3 4
```

## Sample Output 1
```
24 12 8 6
```

## Sample Input 2
```
5
-1 1 0 -3 3
```

## Sample Output 2
```
0 0 9 0 0
```

## Sample Input 3
```
3
2 3 4
```

## Sample Output 3
```
12 8 6
```

## Sample Input 4
```
2
5 10
```

## Sample Output 4
```
10 5
```
""",

    "template.py": """class Solution(object):
    def productExceptSelf(self, nums):
        \"\"\"
        :type nums: List[int]
        :rtype: List[int]
        \"\"\"
        return []
""",

    "template.cpp": """class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums);
};
""",

    "solution.py": """from typing import TextIO, List
import sys

class Solution(object):
    def productExceptSelf(self, nums):
        \"\"\"
        :type nums: List[int]
        :rtype: List[int]
        \"\"\"
        n = len(nums)
        answer = [1] * n
        
        # First pass: calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Second pass: calculate suffix products and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n = int(infile.readline())
    nums = list(map(int, infile.readline().split()))
    
    solution = Solution()
    result = solution.productExceptSelf(nums)
    
    outfile.write(' '.join(map(str, result)) + '\\n')

if __name__ == "__main__":
    solve()
""",

    "solution.cpp": """#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);
        
        // First pass: calculate prefix products
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            answer[i] = prefix;
            prefix *= nums[i];
        }
        
        // Second pass: calculate suffix products and multiply
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= suffix;
            suffix *= nums[i];
        }
        
        return answer;
    }
};

void solve() {
    int n;
    cin >> n;
    
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    Solution solution;
    vector<int> result = solution.productExceptSelf(nums);
    
    for (int i = 0; i < result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
}

int main() {
    solve();
    return 0;
}
""",

    "wrapper.py": """import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        
        solution = Solution()
        result = solution.productExceptSelf(nums)
        
        print(' '.join(map(str, result)))
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
""",

    "wrapper.cpp": """#include <iostream>
#include <vector>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int n;
    cin >> n;
    
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    Solution solution;
    vector<int> result = solution.productExceptSelf(nums);
    
    for (int i = 0; i < result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    
    return 0;
}
""",

    "generator.py": """import random
import json
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            [1, 2],  # Minimal size
            [0, 0],  # All zeros
            [1, 0],  # One zero
            [-1, -2, -3],  # All negative
            [5, 5, 5, 5],  # All same
        ]
        nums = rng.choice(edge_types)
    
    elif rule_type == "small":
        n = rng.randint(2, 10)
        nums = [rng.randint(-30, 30) for _ in range(n)]
    
    elif rule_type == "medium":
        n = rng.randint(10, 100)
        nums = [rng.randint(-30, 30) for _ in range(n)]
    
    elif rule_type == "large":
        n = rng.randint(100, 1000)
        nums = [rng.randint(-30, 30) for _ in range(n)]
    
    elif rule_type == "stress":
        n = rng.randint(1000, 100000)
        nums = [rng.randint(-30, 30) for _ in range(n)]
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Format output
    output = f"{len(nums)}\\n"
    output += ' '.join(map(str, nums)) + '\\n'
    
    return output

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate test cases')
    parser.add_argument('rule_type', type=str, help='Type of test case to generate')
    parser.add_argument('--args', type=str, default='{}', help='Arguments as JSON string')
    parser.add_argument('--rng-seed', type=int, help='Random seed')
    
    args = parser.parse_args()
    
    test_args = json.loads(args.args)
    if args.rng_seed is not None:
        test_args['seed'] = args.rng_seed
    
    result = generate_case(args.rule_type, test_args)
    print(result, end='')
""",

    "config.json": json.dumps({
        "generation_logic": [
            {"type": "edge_cases", "count": 5, "args": {}},
            {"type": "small", "count": 10, "args": {}},
            {"type": "medium", "count": 15, "args": {}},
            {"type": "large", "count": 15, "args": {}},
            {"type": "stress", "count": 10, "args": {}}
        ]
    }, indent=2),

    "examples.json": json.dumps([
        {
            "stdin": "4\\n1 2 3 4\\n",
            "expected_output": "24 12 8 6\\n",
            "visibility": "visible"
        },
        {
            "stdin": "5\\n-1 1 0 -3 3\\n",
            "expected_output": "0 0 9 0 0\\n",
            "visibility": "visible"
        },
        {
            "stdin": "3\\n2 3 4\\n",
            "expected_output": "12 8 6\\n",
            "visibility": "visible"
        },
        {
            "stdin": "2\\n5 10\\n",
            "expected_output": "10 5\\n",
            "visibility": "visible"
        }
    ], indent=2)
}

# Problem 4: Top K Frequent Elements
problem_17_files = {
    "description.txt": """Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

## Input Format
- First line: Two integers n k (array length and k)
- Second line: n space-separated integers

## Output Format
- k space-separated integers (the k most frequent elements in any order)

## Constraints
- 1 ≤ k ≤ n ≤ 10^5
- -10^4 ≤ nums[i] ≤ 10^4
- The answer is guaranteed to be unique

## Sample Input 1
```
6 2
1 1 1 2 2 3
```

## Sample Output 1
```
1 2
```

## Sample Input 2
```
1 1
1
```

## Sample Output 2
```
1
```

## Sample Input 3
```
7 3
4 1 -1 2 -1 2 3
```

## Sample Output 3
```
-1 2 4
```

## Sample Input 4
```
5 1
5 5 5 4 4
```

## Sample Output 4
```
5
```
""",

    "template.py": """class Solution(object):
    def topKFrequent(self, nums, k):
        \"\"\"
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        \"\"\"
        return []
""",

    "template.cpp": """class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k);
};
""",

    "solution.py": """from typing import TextIO, List
import sys

class Solution(object):
    def topKFrequent(self, nums, k):
        \"\"\"
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        \"\"\"
        from collections import Counter
        import heapq
        
        # Count frequencies
        freq = Counter(nums)
        
        # Use heap to get top k
        # Python's heapq is min heap, so negate frequencies for max heap behavior
        return heapq.nlargest(k, freq.keys(), key=freq.get)

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n, k = map(int, infile.readline().split())
    nums = list(map(int, infile.readline().split()))
    
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    
    outfile.write(' '.join(map(str, result)) + '\\n')

if __name__ == "__main__":
    solve()
""",

    "solution.cpp": """#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Count frequencies
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // Use min heap to keep top k elements
        auto cmp = [](pair<int, int>& a, pair<int, int>& b) {
            return a.second > b.second;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> minHeap(cmp);
        
        for (auto& p : freq) {
            minHeap.push(p);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        // Extract results
        vector<int> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top().first);
            minHeap.pop();
        }
        
        return result;
    }
};

void solve() {
    int n, k;
    cin >> n >> k;
    
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    Solution solution;
    vector<int> result = solution.topKFrequent(nums, k);
    
    for (int i = 0; i < result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
}

int main() {
    solve();
    return 0;
}
""",

    "wrapper.py": """import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        
        solution = Solution()
        result = solution.topKFrequent(nums, k)
        
        print(' '.join(map(str, result)))
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
""",

    "wrapper.cpp": """#include <iostream>
#include <vector>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int n, k;
    cin >> n >> k;
    
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    Solution solution;
    vector<int> result = solution.topKFrequent(nums, k);
    
    for (int i = 0; i < result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    
    return 0;
}
""",

    "generator.py": """import random
import json
import sys
from collections import Counter

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_types = [
            ([1], 1),
            ([1, 2], 1),
            ([1, 1, 2, 2, 3], 2),
            ([5, 5, 5, 5], 1),
            ([1, 2, 3, 4, 5], 5),
        ]
        nums, k = rng.choice(edge_types)
    
    elif rule_type == "small":
        n = rng.randint(1, 10)
        k = rng.randint(1, n)
        nums = [rng.randint(-100, 100) for _ in range(n)]
    
    elif rule_type == "medium":
        n = rng.randint(10, 100)
        k = rng.randint(1, min(20, n))
        nums = [rng.randint(-1000, 1000) for _ in range(n)]
    
    elif rule_type == "large":
        n = rng.randint(100, 1000)
        k = rng.randint(1, min(50, n))
        nums = [rng.randint(-10000, 10000) for _ in range(n)]
    
    elif rule_type == "stress":
        n = rng.randint(1000, 100000)
        k = rng.randint(1, min(100, n))
        nums = [rng.randint(-10000, 10000) for _ in range(n)]
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Format output
    output = f"{len(nums)} {k}\\n"
    output += ' '.join(map(str, nums)) + '\\n'
    
    return output

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate test cases')
    parser.add_argument('rule_type', type=str, help='Type of test case to generate')
    parser.add_argument('--args', type=str, default='{}', help='Arguments as JSON string')
    parser.add_argument('--rng-seed', type=int, help='Random seed')
    
    args = parser.parse_args()
    
    test_args = json.loads(args.args)
    if args.rng_seed is not None:
        test_args['seed'] = args.rng_seed
    
    result = generate_case(args.rule_type, test_args)
    print(result, end='')
""",

    "config.json": json.dumps({
        "generation_logic": [
            {"type": "edge_cases", "count": 5, "args": {}},
            {"type": "small", "count": 10, "args": {}},
            {"type": "medium", "count": 15, "args": {}},
            {"type": "large", "count": 15, "args": {}},
            {"type": "stress", "count": 10, "args": {}}
        ]
    }, indent=2),

    "examples.json": json.dumps([
        {
            "stdin": "6 2\\n1 1 1 2 2 3\\n",
            "expected_output": "1 2\\n",
            "visibility": "visible"
        },
        {
            "stdin": "1 1\\n1\\n",
            "expected_output": "1\\n",
            "visibility": "visible"
        },
        {
            "stdin": "7 3\\n4 1 -1 2 -1 2 3\\n",
            "expected_output": "-1 2 4\\n",
            "visibility": "visible"
        },
        {
            "stdin": "5 1\\n5 5 5 4 4\\n",
            "expected_output": "5\\n",
            "visibility": "visible"
        }
    ], indent=2)
}

# Problem 5: Elevator Control System
problem_18_files = {
    "description.txt": """Elevator Control System

Design an object-oriented system to control elevators in a building.
Implement a simplified simulation that processes a sequence of requests.

## Input Format
- Line 1: Three integers N M T (floors, elevators, time steps)
- Next T lines: Requests in format "EXTERNAL floor direction" or "INTERNAL elevator_id destination"

## Output Format
- For each time step, print elevator action in the format shown in examples

## Constraints
- 2 ≤ N ≤ 100
- 1 ≤ M ≤ 10
- 1 ≤ T ≤ 100
- Directions: UP, DOWN
- Simple dispatching: use nearest idle elevator

## Sample Input 1
```
10 2 5
EXTERNAL 3 UP
INTERNAL 0 7
EXTERNAL 5 DOWN
INTERNAL 1 2
EXTERNAL 8 DOWN
```

## Sample Output 1
```
Step 0: Elevator 0 dispatched to floor 3
Step 1: Elevator 0 moving to floor 7
Step 2: Elevator 1 dispatched to floor 5
Step 3: Elevator 1 moving to floor 2
Step 4: Elevator 0 dispatched to floor 8
```

## Sample Input 2
```
5 1 2
EXTERNAL 2 UP
INTERNAL 0 4
```

## Sample Output 2
```
Step 0: Elevator 0 dispatched to floor 2
Step 1: Elevator 0 moving to floor 4
```

## Sample Input 3
```
8 3 3
EXTERNAL 4 UP
EXTERNAL 6 DOWN
INTERNAL 1 3
```

## Sample Output 3
```
Step 0: Elevator 0 dispatched to floor 4
Step 1: Elevator 1 dispatched to floor 6
Step 2: Elevator 1 moving to floor 3
```
""",

    "template.py": """class Solution(object):
    def simulateElevatorSystem(self, numFloors, numElevators, requests):
        \"\"\"
        :type numFloors: int
        :type numElevators: int
        :type requests: List[str]
        :rtype: List[str]
        \"\"\"
        return []
""",

    "template.cpp": """class Solution {
public:
    vector<string> simulateElevatorSystem(int numFloors, int numElevators, 
                                          vector<string>& requests);
};
""",

    "solution.py": """from typing import TextIO, List
import sys
from collections import deque

class Solution(object):
    def simulateElevatorSystem(self, numFloors, numElevators, requests):
        \"\"\"
        :type numFloors: int
        :type numElevators: int
        :type requests: List[str]
        :rtype: List[str]
        \"\"\"
        class Elevator:
            def __init__(self, elevator_id):
                self.id = elevator_id
                self.current_floor = 1
                self.direction = "IDLE"
                self.state = "IDLE"
                self.destinations = deque()
        
        elevators = [Elevator(i) for i in range(numElevators)]
        output = []
        step = 0
        
        for req in requests:
            parts = req.split()
            req_type = parts[0]
            
            if req_type == "EXTERNAL":
                floor = int(parts[1])
                direction = parts[2]
                
                # Simple dispatch: find nearest idle elevator
                best_elev = 0
                min_dist = abs(elevators[0].current_floor - floor)
                
                for i in range(1, numElevators):
                    dist = abs(elevators[i].current_floor - floor)
                    if dist < min_dist:
                        min_dist = dist
                        best_elev = i
                
                elevators[best_elev].destinations.append(floor)
                output.append(f"Step {step}: Elevator {best_elev} dispatched to floor {floor}")
                
            elif req_type == "INTERNAL":
                elev_id = int(parts[1])
                dest = int(parts[2])
                
                if 0 <= elev_id < numElevators:
                    elevators[elev_id].destinations.append(dest)
                    output.append(f"Step {step}: Elevator {elev_id} moving to floor {dest}")
            
            step += 1
        
        return output

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n, m, t = map(int, infile.readline().split())
    requests = []
    for _ in range(t):
        requests.append(infile.readline().strip())
    
    solution = Solution()
    output = solution.simulateElevatorSystem(n, m, requests)
    
    for line in output:
        outfile.write(line + '\\n')

if __name__ == "__main__":
    solve()
""",

    "solution.cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <sstream>
#include <cmath>
using namespace std;

class Solution {
private:
    enum Direction { IDLE, UP, DOWN };
    enum State { STOPPED, MOVING, DOORS_OPEN };
    
    struct Elevator {
        int id;
        int currentFloor;
        Direction direction;
        State state;
        queue<int> destinations;
        
        Elevator(int id) : id(id), currentFloor(1), direction(IDLE), state(STOPPED) {}
    };
    
public:
    vector<string> simulateElevatorSystem(int numFloors, int numElevators, 
                                          vector<string>& requests) {
        vector<Elevator> elevators;
        for (int i = 0; i < numElevators; i++) {
            elevators.push_back(Elevator(i));
        }
        
        vector<string> output;
        int step = 0;
        
        for (const string& req : requests) {
            istringstream iss(req);
            string type;
            iss >> type;
            
            if (type == "EXTERNAL") {
                int floor;
                string dir;
                iss >> floor >> dir;
                
                // Simple dispatch: find nearest idle elevator
                int bestElev = 0;
                int minDist = abs(elevators[0].currentFloor - floor);
                
                for (int i = 1; i < numElevators; i++) {
                    int dist = abs(elevators[i].currentFloor - floor);
                    if (dist < minDist) {
                        minDist = dist;
                        bestElev = i;
                    }
                }
                
                elevators[bestElev].destinations.push(floor);
                output.push_back("Step " + to_string(step) + 
                               ": Elevator " + to_string(bestElev) + 
                               " dispatched to floor " + to_string(floor));
            }
            else if (type == "INTERNAL") {
                int elevId, dest;
                iss >> elevId >> dest;
                
                if (elevId >= 0 && elevId < numElevators) {
                    elevators[elevId].destinations.push(dest);
                    output.push_back("Step " + to_string(step) + 
                                   ": Elevator " + to_string(elevId) + 
                                   " moving to floor " + to_string(dest));
                }
            }
            
            step++;
        }
        
        return output;
    }
};

void solve() {
    int n, m, t;
    cin >> n >> m >> t;
    cin.ignore();
    
    vector<string> requests;
    for (int i = 0; i < t; i++) {
        string line;
        getline(cin, line);
        requests.push_back(line);
    }
    
    Solution solution;
    vector<string> output = solution.simulateElevatorSystem(n, m, requests);
    
    for (const string& line : output) {
        cout << line << endl;
    }
}

int main() {
    solve();
    return 0;
}
""",

    "wrapper.py": """import sys

# ===== PLATFORM INJECTION POINT =====
# The contestant's Solution class will be injected here by the platform
# DO NOT UNCOMMENT OR MODIFY THIS SECTION
# ===== END INJECTION POINT =====

def main():
    try:
        n, m, t = map(int, input().split())
        requests = []
        for _ in range(t):
            requests.append(input().strip())
        
        solution = Solution()
        output = solution.simulateElevatorSystem(n, m, requests)
        
        for line in output:
            print(line)
            
    except Exception as e:
        print(f"Runtime Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
""",

    "wrapper.cpp": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int n, m, t;
    cin >> n >> m >> t;
    cin.ignore();
    
    vector<string> requests;
    for (int i = 0; i < t; i++) {
        string line;
        getline(cin, line);
        requests.push_back(line);
    }
    
    Solution solution;
    vector<string> output = solution.simulateElevatorSystem(n, m, requests);
    
    for (const string& line : output) {
        cout << line << endl;
    }
    
    return 0;
}
""",

    "generator.py": """import random
import json
import sys

def generate_case(rule_type, args):
    rng = random.Random(args.get("seed"))
    
    if rule_type == "edge_cases":
        edge_configs = [
            (5, 1, 2),   # Single elevator
            (10, 2, 3),  # Two elevators
            (3, 3, 1),   # More elevators than needed
            (20, 5, 5),  # Multiple elevators
            (10, 1, 1),  # Single request
        ]
        numFloors, numElevators, numRequests = rng.choice(edge_configs)
    
    elif rule_type == "small":
        numFloors = rng.randint(5, 10)
        numElevators = rng.randint(1, 3)
        numRequests = rng.randint(2, 5)
    
    elif rule_type == "medium":
        numFloors = rng.randint(10, 30)
        numElevators = rng.randint(2, 5)
        numRequests = rng.randint(5, 20)
    
    elif rule_type == "large":
        numFloors = rng.randint(30, 70)
        numElevators = rng.randint(3, 8)
        numRequests = rng.randint(20, 50)
    
    elif rule_type == "stress":
        numFloors = rng.randint(70, 100)
        numElevators = rng.randint(5, 10)
        numRequests = rng.randint(50, 100)
    
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    # Generate requests
    requests = []
    for _ in range(numRequests):
        if rng.random() < 0.5:  # EXTERNAL request
            floor = rng.randint(2, numFloors)
            direction = rng.choice(["UP", "DOWN"])
            requests.append(f"EXTERNAL {floor} {direction}")
        else:  # INTERNAL request
            elevator_id = rng.randint(0, numElevators - 1)
            dest = rng.randint(1, numFloors)
            requests.append(f"INTERNAL {elevator_id} {dest}")
    
    # Format output
    output = f"{numFloors} {numElevators} {numRequests}\\n"
    for req in requests:
        output += f"{req}\\n"
    
    return output

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate test cases')
    parser.add_argument('rule_type', type=str, help='Type of test case to generate')
    parser.add_argument('--args', type=str, default='{}', help='Arguments as JSON string')
    parser.add_argument('--rng-seed', type=int, help='Random seed')
    
    args = parser.parse_args()
    
    test_args = json.loads(args.args)
    if args.rng_seed is not None:
        test_args['seed'] = args.rng_seed
    
    result = generate_case(args.rule_type, test_args)
    print(result, end='')
""",

    "config.json": json.dumps({
        "generation_logic": [
            {"type": "edge_cases", "count": 5, "args": {}},
            {"type": "small", "count": 10, "args": {}},
            {"type": "medium", "count": 15, "args": {}},
            {"type": "large", "count": 15, "args": {}},
            {"type": "stress", "count": 10, "args": {}}
        ]
    }, indent=2),

    "examples.json": json.dumps([
        {
            "stdin": "10 2 5\\nEXTERNAL 3 UP\\nINTERNAL 0 7\\nEXTERNAL 5 DOWN\\nINTERNAL 1 2\\nEXTERNAL 8 DOWN\\n",
            "expected_output": "Step 0: Elevator 0 dispatched to floor 3\\nStep 1: Elevator 0 moving to floor 7\\nStep 2: Elevator 1 dispatched to floor 5\\nStep 3: Elevator 1 moving to floor 2\\nStep 4: Elevator 0 dispatched to floor 8\\n",
            "visibility": "visible"
        },
        {
            "stdin": "5 1 2\\nEXTERNAL 2 UP\\nINTERNAL 0 4\\n",
            "expected_output": "Step 0: Elevator 0 dispatched to floor 2\\nStep 1: Elevator 0 moving to floor 4\\n",
            "visibility": "visible"
        },
        {
            "stdin": "8 3 3\\nEXTERNAL 4 UP\\nEXTERNAL 6 DOWN\\nINTERNAL 1 3\\n",
            "expected_output": "Step 0: Elevator 0 dispatched to floor 4\\nStep 1: Elevator 1 dispatched to floor 6\\nStep 2: Elevator 1 moving to floor 3\\n",
            "visibility": "visible"
        }
    ], indent=2)
}

# Create all problems
def create_problem(problem_name, files_dict):
    """Create a problem directory with all files"""
    problem_dir = os.path.join(BASE_DIR, problem_name)
    os.makedirs(problem_dir, exist_ok=True)
    
    for filename, content in files_dict.items():
        filepath = os.path.join(problem_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)
    
    print(f"✓ Created {problem_name} with {len(files_dict)} files")

def main():
    # Create base directory
    os.makedirs(BASE_DIR, exist_ok=True)
    
    problems = [
        ("problem_14_merge_overlapping_intervals", problem_14_files),
        ("problem_15_number_of_islands", problem_15_files),
        ("problem_16_product_of_array_except_self", problem_16_files),
        ("problem_17_top_k_frequent_elements", problem_17_files),
        ("problem_18_elevator_control_system", problem_18_files),
    ]
    
    print("Generating 31_oct_level_2 problems following 30_oct/ canonical format...\\n")
    
    for problem_name, files in problems:
        create_problem(problem_name, files)
    
    print("\\n✓ All problems generated successfully!")
    print(f"\\nCreated in: {BASE_DIR}/")
    print("  ├── problem_14_merge_overlapping_intervals/")
    print("  ├── problem_15_number_of_islands/")
    print("  ├── problem_16_product_of_array_except_self/")
    print("  ├── problem_17_top_k_frequent_elements/")
    print("  └── problem_18_elevator_control_system/")
    print("\\nEach problem contains 10 files:")
    print("  ├── description.txt")
    print("  ├── template.py")
    print("  ├── template.cpp")
    print("  ├── solution.py")
    print("  ├── solution.cpp")
    print("  ├── wrapper.py")
    print("  ├── wrapper.cpp")
    print("  ├── generator.py")
    print("  ├── config.json")
    print("  └── examples.json")
    print("\\nNext steps:")
    print("  1. Review the generated files")
    print("  2. Run smoke tests from templates/smoke_test.md")
    print("  3. Generate test suites with orchestrator.py")

if __name__ == "__main__":
    main()
