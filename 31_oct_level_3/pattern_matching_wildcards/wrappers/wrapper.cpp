#include <iostream>
#include <string>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The platform will inject the contestant's Solution class here.
// It must define:
//   class Solution {
//   public:
//       bool isMatch(string s, string p);
//   };
// ===== END PLATFORM INJECTION POINT =====

int main() {
    string s, p;
    getline(cin, s);
    getline(cin, p);
    
    Solution solution;
    bool result = solution.isMatch(s, p);
    cout << (result ? "true" : "false") << endl;
    
    return 0;
}
