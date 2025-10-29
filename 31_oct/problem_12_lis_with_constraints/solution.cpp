#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return 0;
        
        // dp[i] = length of longest increasing subsequence ending at index i
        vector<int> dp(n, 1);
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                // Check if nums[i] > nums[j] and difference constraint satisfied
                if (nums[i] > nums[j] && (long long)(nums[i] - nums[j]) <= k) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        
        return *max_element(dp.begin(), dp.end());
    }
};

int main() {
    int n, k;
    cin >> n >> k;
    
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    Solution solution;
    int result = solution.lengthOfLIS(nums, k);
    cout << result << endl;
    
    return 0;
}
