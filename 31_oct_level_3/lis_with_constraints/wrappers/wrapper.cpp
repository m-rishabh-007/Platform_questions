#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The platform will inject the contestant's Solution class here.
// It must define:
//   class Solution {
//   public:
//       int lengthOfLIS(vector<int>& nums, int k);
//   };
// ===== END PLATFORM INJECTION POINT =====

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
