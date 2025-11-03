#include <iostream>
using namespace std;

class Solution {
public:
    long long total_branches(int n) {
        if (n == 0) return 1;
        if (n == 1) return 2;
        if (n == 2) return 4;
        
        // Calculate Tribonacci values (new branches at each level)
        long long trib0 = 1, trib1 = 1, trib2 = 2;
        long long total = 1 + 1 + 2; // Sum of first 3 levels
        
        for (int i = 3; i <= n; i++) {
            long long newBranches = trib0 + trib1 + trib2;
            total += newBranches;
            
            trib0 = trib1;
            trib1 = trib2;
            trib2 = newBranches;
        }
        
        return total;
    }
};

int main() {
    int n;
    cin >> n;
    
    Solution solution;
    cout << solution.total_branches(n) << endl;
    
    return 0;
}
