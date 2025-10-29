#include <iostream>
#include <vector>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int n;
    cin >> n;
    
    vector<vector<int>> treeData;
    for (int i = 0; i < n; i++) {
        int node_id, parent_id, value;
        cin >> node_id >> parent_id >> value;
        treeData.push_back({node_id, parent_id, value});
    }
    
    int p, q;
    cin >> p >> q;
    
    Solution solution;
    cout << solution.lowestCommonAncestor(treeData, p, q) << endl;
    
    return 0;
}
