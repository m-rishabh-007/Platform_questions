#include <iostream>
#include <vector>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }
    
    Solution solution;
    cout << solution.countComponents(n, edges) << endl;
    
    return 0;
}
