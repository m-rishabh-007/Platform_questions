#include <iostream>
#include <vector>
#include <string>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int m, n;
    cin >> m >> n;
    
    vector<vector<char>> grid(m, vector<char>(n));
    for (int i = 0; i < m; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < n; j++) {
            grid[i][j] = row[j];
        }
    }
    
    Solution solution;
    cout << solution.numIslands(grid) << endl;
    
    return 0;
}
