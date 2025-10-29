#!/usr/bin/env python3
"""
Batch create all remaining files for 31_oct problems 07-10
"""
import os

# Problem 07: Solution Python
solution_py_07 = '''import sys
from typing import TextIO
from functools import lru_cache

class Solution(object):
    def maxProduct(self, nums, k, limit):
        """
        :type nums: List[int]
        :type k: int
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def dp(idx, current_sum, length):
            # Base case
            if idx == n:
                if current_sum == k and length > 0:
                    return 1
                return -1
            
            # Skip current element
            result = dp(idx + 1, current_sum, length)
            
            # Take current element
            sign = 1 if length % 2 == 0 else -1
            new_sum = current_sum + sign * nums[idx]
            sub_result = dp(idx + 1, new_sum, length + 1)
            
            if sub_result != -1:
                product = sub_result * nums[idx]
                if product <= limit:
                    result = max(result, product)
            
            return result
        
        return dp(0, 0, 0)

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """For orchestrator.py execution"""
    line = infile.readline().split()
    n = int(line[0])
    k = int(line[1])
    limit = int(line[2])
    
    nums = list(map(int, infile.readline().split()))
    
    solution = Solution()
    result = solution.maxProduct(nums, k, limit)
    outfile.write(str(result) + '\\n')

if __name__ == "__main__":
    solve()
'''

with open('31_oct/problem_07_max_product_alternating/solution.py', 'w') as f:
    f.write(solution_py_07)

# Problem 07: Solution C++
solution_cpp_07 = '''#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <functional>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        int n = nums.size();
        map<tuple<int, int, int>, int> dp;
        
        function<int(int, int, int)> solve = [&](int idx, int sum, int parity) -> int {
            if (idx == n) {
                return (sum == k && parity == 1) ? 1 : -1;
            }
            
            auto key = make_tuple(idx, sum, parity);
            if (dp.count(key)) return dp[key];
            
            // Skip current element
            int result = solve(idx + 1, sum, parity);
            
            // Take current element
            int sign = (parity == 0) ? 1 : -1;
            int newSum = sum + sign * nums[idx];
            int subResult = solve(idx + 1, newSum, 1 - parity);
            
            if (subResult != -1) {
                long long product = (long long)subResult * nums[idx];
                if (product <= limit) {
                    result = max(result, (int)product);
                }
            }
            
            return dp[key] = result;
        };
        
        return solve(0, 0, 0);
    }
};

int main() {
    int n, k, limit;
    cin >> n >> k >> limit;
    
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    Solution solution;
    cout << solution.maxProduct(nums, k, limit) << endl;
    
    return 0;
}
'''

with open('31_oct/problem_07_max_product_alternating/solution.cpp', 'w') as f:
    f.write(solution_cpp_07)

print('✓ Created problem_07 solutions')
