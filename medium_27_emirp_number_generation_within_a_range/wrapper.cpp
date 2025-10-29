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
//     vector<int> find_emirps_in_range(int limit) {
//         return {};
//     }
// };
// ===== END INJECTION POINT =====

void execute_solution() {
    int limit;
    cin >> limit;
    
    Solution solution;
    auto result = solution.find_emirps_in_range(limit);
    
    if (!result.empty()) {
        for (size_t i = 0; i < result.size(); i++) {
            cout << result[i];
            if (i + 1 < result.size()) {
                cout << " ";
            }
        }
    }
    cout << "\n";
}

int main() {
    execute_solution();
    return 0;
}