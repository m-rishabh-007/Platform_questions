class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        return 0;
    }
};
#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <functional>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

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
