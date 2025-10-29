#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        
        // Sort intervals by start time
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> merged;
        merged.push_back(intervals[0]);
        
        for (int i = 1; i < intervals.size(); i++) {
            // If current interval overlaps with the last merged interval
            if (intervals[i][0] <= merged.back()[1]) {
                // Merge by updating the end time
                merged.back()[1] = max(merged.back()[1], intervals[i][1]);
            } else {
                // No overlap, add as new interval
                merged.push_back(intervals[i]);
            }
        }
        
        return merged;
    }
};

void solve() {
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
}

int main() {
    solve();
    return 0;
}
