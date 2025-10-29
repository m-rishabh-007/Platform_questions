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
    string capitalizeWords(const string& sentence) {
        istringstream iss(sentence);
        string word;
        vector<string> words;
        
        while (iss >> word) {
            if (!word.empty()) {
                word[0] = toupper(word[0]);
                for (size_t i = 1; i < word.length(); i++) {
                    word[i] = tolower(word[i]);
                }
                words.push_back(word);
            }
        }
        
        string result;
        for (size_t i = 0; i < words.size(); i++) {
            result += words[i];
            if (i < words.size() - 1) result += " ";
        }
        
        return result;
    }
};

void solve(istream& in = cin, ostream& out = cout) {
    // Read input
    string sentence;
    getline(in, sentence);
    
    // Create solution instance and call the method
    Solution solution;
    string result = solution.capitalizeWords(sentence);
    
    // Output the result
    out << result << endl;
}

int main() {
    solve();
    return 0;
}
