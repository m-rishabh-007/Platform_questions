#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long maxEnergy(int n, int m, int h, vector<int>& capacity, vector<int>& power) {
        // Sort both arrays in descending order to pair largest with largest
        sort(capacity.begin(), capacity.end(), greater<int>());
        sort(power.begin(), power.end(), greater<int>());
        
        long long totalEnergy = 0;
        int pairs = min(n, m);
        
        for (int i = 0; i < pairs; i++) {
            // Energy that can be generated in h hours
            long long generatedEnergy = (long long)power[i] * h;
            // Take minimum of generated and capacity
            totalEnergy += min(generatedEnergy, (long long)capacity[i]);
        }
        
        return totalEnergy;
    }
};

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n, m, h;
        cin >> n >> m >> h;
        
        vector<int> capacity(n), power(m);
        for (int i = 0; i < n; i++) {
            cin >> capacity[i];
        }
        for (int i = 0; i < m; i++) {
            cin >> power[i];
        }
        
        Solution solution;
        long long result = solution.maxEnergy(n, m, h, capacity, power);
        cout << result << endl;
    }
    
    return 0;
}
