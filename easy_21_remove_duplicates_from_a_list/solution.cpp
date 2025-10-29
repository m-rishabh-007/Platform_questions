#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> removeDuplicates(const vector<int>& numbers) {
        unordered_set<int> seen;
        vector<int> result;
        
        for (int num : numbers) {
            if (seen.find(num) == seen.end()) {
                seen.insert(num);
                result.push_back(num);
            }
        }
        
        return result;
    }
};

void solve(istream& in = cin, ostream& out = cout) {
    // Read input
    int n;
    in >> n;
    
    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        in >> numbers[i];
    }
    
    // Create solution instance and call the method
    Solution solution;
    vector<int> result = solution.removeDuplicates(numbers);
    
    // Output the result
    for (size_t i = 0; i < result.size(); i++) {
        out << result[i];
        if (i < result.size() - 1) out << " ";
    }
    out << endl;
}

int main() {
    solve();
    return 0;
}
