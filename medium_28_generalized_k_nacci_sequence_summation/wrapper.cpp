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
//     long long sum_k_nacci_sequence(int n, int k) {
//         return 0;
//     }
// };
// ===== END INJECTION POINT =====

void execute_solution() {
    int n, k;
    cin >> n >> k;
    
    Solution solution;
    auto result = solution.sum_k_nacci_sequence(n, k);
    
    cout << result << "\n";
}

int main() {
    execute_solution();
    return 0;
}