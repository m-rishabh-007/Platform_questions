#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Count frequencies
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // Use min heap to keep top k elements
        auto cmp = [](pair<int, int>& a, pair<int, int>& b) {
            return a.second > b.second;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> minHeap(cmp);
        
        for (auto& p : freq) {
            minHeap.push(p);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        // Extract results
        vector<int> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top().first);
            minHeap.pop();
        }
        
        // Sort result for consistent output
        sort(result.begin(), result.end());
        
        return result;
    }
};

void solve() {
    int n, k;
    cin >> n >> k;
    
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    Solution solution;
    vector<int> result = solution.topKFrequent(nums, k);
    
    for (int i = 0; i < result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
}

int main() {
    solve();
    return 0;
}
