#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length(), n = p.length();
        
        // dp[i][j] = true if s[0..i-1] matches p[0..j-1]
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Empty string matches empty pattern
        dp[0][0] = true;
        
        // Handle patterns like *, **, ***, etc. at the beginning
        for (int j = 1; j <= n; j++) {
            if (p[j-1] == '*') {
                dp[0][j] = dp[0][j-1];
            }
        }
        
        // Fill the DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j-1] == '*') {
                    // * can match empty sequence or one/more characters
                    dp[i][j] = dp[i][j-1] || dp[i-1][j];
                } else if (p[j-1] == '?' || s[i-1] == p[j-1]) {
                    // ? matches any single char, or exact character match
                    dp[i][j] = dp[i-1][j-1];
                }
            }
        }
        
        return dp[m][n];
    }
};

int main() {
    string s, p;
    getline(cin, s);
    getline(cin, p);
    
    Solution solution;
    bool result = solution.isMatch(s, p);
    cout << (result ? "true" : "false") << endl;
    
    return 0;
}
