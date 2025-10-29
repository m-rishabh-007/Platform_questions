#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int lowestCommonAncestor(vector<vector<int>>& treeData, int p, int q) {
        unordered_map<int, int> valueToId;
        unordered_map<int, int> idToParent;
        unordered_map<int, int> idToValue;
        
        for (const auto& node : treeData) {
            int node_id = node[0];
            int parent_id = node[1];
            int value = node[2];
            
            valueToId[value] = node_id;
            idToParent[node_id] = parent_id;
            idToValue[node_id] = value;
        }
        
        int p_id = valueToId[p];
        int q_id = valueToId[q];
        
        // Get ancestors of p
        unordered_set<int> p_ancestors;
        int current = p_id;
        while (current != -1) {
            p_ancestors.insert(current);
            current = idToParent.count(current) ? idToParent[current] : -1;
        }
        
        // Find first common ancestor from q
        current = q_id;
        while (current != -1) {
            if (p_ancestors.count(current)) {
                return idToValue[current];
            }
            current = idToParent.count(current) ? idToParent[current] : -1;
        }
        
        return -1;
    }
};

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
