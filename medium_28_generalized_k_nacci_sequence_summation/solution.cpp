#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    long long sum_k_nacci_sequence(int n, int k) {
        if (n < 0) {
            return 0;
        }
        
        // If n is less than k, we only have base cases (all 1s)
        if (n < k) {
            return n + 1;
        }
        
        // Initialize the first k terms (all 1s)
        vector<long long> terms(k, 1);
        long long total_sum = k;  // Sum of first k terms
        
        // Calculate terms from index k to n
        for (int i = k; i <= n; i++) {
            // Calculate the next term as sum of previous k terms
            long long next_term = 0;
            for (int j = 0; j < k; j++) {
                next_term += terms[j];
            }
            total_sum += next_term;
            
            // Update the sliding window by shifting left and adding new term
            for (int j = 0; j < k - 1; j++) {
                terms[j] = terms[j + 1];
            }
            terms[k - 1] = next_term;
        }
        
        return total_sum;
    }
};

void solve(istream& in = cin, ostream& out = cout) {
    int n, k;
    in >> n >> k;
    
    Solution solution;
    auto result = solution.sum_k_nacci_sequence(n, k);
    
    out << result << "\n";
}

int main() {
    solve();
    return 0;
}