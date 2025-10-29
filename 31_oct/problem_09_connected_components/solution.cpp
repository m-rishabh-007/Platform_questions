#include <iostream>
#include <vector>
#include <unordered_set>
#include <sstream>
using namespace std;

class Solution {
private:
    void dfs(int node, vector<vector<int>>& graph, vector<bool>& visited) {
        visited[node] = true;
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, graph, visited);
            }
        }
    }
    
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        // Build adjacency list
        vector<vector<int>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<bool> visited(n, false);
        int components = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, graph, visited);
                components++;
            }
        }
        
        return components;
    }
};

int main() {
    int n, m;
    cin >> n >> m;
    cin.ignore(); // Ignore the newline after n and m
    
    vector<vector<int>> edges;
    for (int i = 0; i < m; i++) {
        string line;
        getline(cin, line);
        if (!line.empty()) {
            istringstream iss(line);
            int u, v;
            iss >> u >> v;
            edges.push_back({u, v});
        }
    }
    
    Solution solution;
    int result = solution.countComponents(n, edges);
    cout << result << endl;
    
    return 0;
}
