#include <iostream>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// ===== END INJECTION POINT =====

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    Solution solution;
    int result = solution.findLargestOfThree(a, b, c);
    cout << result << endl;
    return 0;
}
