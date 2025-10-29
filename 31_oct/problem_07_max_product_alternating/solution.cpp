#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <functional>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        int n = nums.size();
        // dp[i][sum][parity] = max product using first i elements, 
        // with alternating sum 'sum', and parity (0=even, 1=odd length)
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
    int result = solution.maxProduct(nums, k, limit);
    cout << result << endl;
    
    return 0;
}
