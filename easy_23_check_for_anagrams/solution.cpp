#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>
#include <cctype>

using namespace std;

class Solution {
public:
    bool isAnagram(const string& str1, const string& str2) {
        // Clean strings: remove spaces and convert to lowercase
        string clean_str1, clean_str2;
        
        for (char c : str1) {
            if (c != ' ') {
                clean_str1 += tolower(c);
            }
        }
        
        for (char c : str2) {
            if (c != ' ') {
                clean_str2 += tolower(c);
            }
        }
        
        // Sort and compare
        sort(clean_str1.begin(), clean_str1.end());
        sort(clean_str2.begin(), clean_str2.end());
        
        return clean_str1 == clean_str2;
    }
};

void solve(istream& in = cin, ostream& out = cout) {
    // Read input
    string str1, str2;
    getline(in, str1);
    getline(in, str2);
    
    // Create solution instance and call the method
    Solution solution;
    bool result = solution.isAnagram(str1, str2);
    
    // Output the result
    out << (result ? "True" : "False") << endl;
}

int main() {
    solve();
    return 0;
}
