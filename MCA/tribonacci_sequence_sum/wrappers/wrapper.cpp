#include <iostream>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// ===== END INJECTION POINT =====

int main() {
    int n;
    cin >> n;
    
    Solution solution;
    cout << solution.total_branches(n) << endl;
    
    return 0;
}
