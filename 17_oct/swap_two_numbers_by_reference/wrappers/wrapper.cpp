#include <iostream>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// ===== END INJECTION POINT =====

int main() {
    int a, b;
    cin >> a >> b;
    Solution solution;
    solution.swapNumbers(a, b);
    cout << a << " " << b << endl;
    return 0;
}
