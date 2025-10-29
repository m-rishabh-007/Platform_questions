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
//     vector<int> calculate_partition_plan(const vector<int>& data_volumes) {
//         return {0, 0};
//     }
// };
// ===== END INJECTION POINT =====

void execute_solution() {
    int n;
    cin >> n;
    
    vector<int> data_volumes(n);
    for (int i = 0; i < n; i++) {
        cin >> data_volumes[i];
    }
    
    Solution solution;
    auto result = solution.calculate_partition_plan(data_volumes);
    
    cout << result[0] << " " << result[1] << "\n";
}

int main() {
    execute_solution();
    return 0;
}