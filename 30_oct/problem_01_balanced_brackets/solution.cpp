using namespace std;
#include <iostream>
#include <string>
#include <stack>
#include <map>

class Solution {
public:
    bool areBracketsBalanced(const string& s) {
        stack<char> st;
        map<char, char> bracket_map;
        bracket_map[')'] = '(';
        bracket_map['}'] = '{';
        bracket_map[']'] = '[';

        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];
            if (bracket_map.find(c) == bracket_map.end()) {
                st.push(c);
            } else {
                if (st.empty() || st.top() != bracket_map[c]) {
                    return false;
                }
                st.pop();
            }
        }
        return st.empty();
    }
};

int main() {
    string s;
    getline(cin, s);
    
    Solution sol;
    if (sol.areBracketsBalanced(s)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
    
    return 0;
}
