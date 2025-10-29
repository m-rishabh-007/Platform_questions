#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int t;
    cin >> t;
    
    Solution solution;
    
    while (t--) {
        int n, m, h;
        cin >> n >> m >> h;
        
        vector<int> capacity(n);
        for (int i = 0; i < n; i++) {
            cin >> capacity[i];
        }
        
        vector<int> power(m);
        for (int i = 0; i < m; i++) {
            cin >> power[i];
        }
        
        cout << solution.maxEnergy(n, m, h, capacity, power) << endl;
    }
    
    return 0;
}
