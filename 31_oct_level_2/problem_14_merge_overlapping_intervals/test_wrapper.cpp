#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals);
};


int main() {
    int n;
    cin >> n;
    
    vector<vector<int>> intervals(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> intervals[i][0] >> intervals[i][1];
    }
    
    Solution solution;
    vector<vector<int>> result = solution.merge(intervals);
    
    for (const auto& interval : result) {
        cout << interval[0] << " " << interval[1] << endl;
    }
    
    return 0;
}
