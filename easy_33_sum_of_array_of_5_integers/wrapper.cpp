#include <iostream>
#include <vector>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// ===== END INJECTION POINT =====

int main() {
    vector<int> arr(5);
    for (int i = 0; i < 5; ++i) {
        cin >> arr[i];
    }
    Solution solution;
    int result = solution.sumOfFive(arr);
    cout << result << endl;
    return 0;
}
