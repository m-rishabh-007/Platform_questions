#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// Example of what gets injected:
// class Solution {
// public:
//     vector<int> analyze_sort_performance(const vector<int>& arr) {
//         return {0, 0};
//     }
// };
// ===== END INJECTION POINT =====

void execute_solution() {
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    Solution solution;
    auto result = solution.analyze_sort_performance(arr);
    
    cout << result[0] << " " << result[1] << "\n";
}

int main() {
    execute_solution();
    return 0;
}