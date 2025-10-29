#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

class Solution {
private:
    string toLower(string s) {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        return s;
    }
    
    bool contains(const string& text, const vector<string>& keywords) {
        for (const string& keyword : keywords) {
            if (text.find(keyword) != string::npos) {
                return true;
            }
        }
        return false;
    }
    
    bool containsWord(const string& text, const vector<string>& words) {
        // Check if word exists as separate word or at start of message
        for (const string& word : words) {
            // Check if starts with word
            if (text.find(word) == 0) {
                return true;
            }
            // Check for word boundaries (space before)
            string pattern = " " + word;
            if (text.find(pattern) != string::npos) {
                return true;
            }
        }
        return false;
    }
    
public:
    vector<string> chatbotResponses(vector<string>& messages) {
        vector<string> responses;
        
        for (const string& msg : messages) {
            string msg_lower = toLower(msg);
            
            // Check for greetings (word boundaries or starts with)
            if (containsWord(msg_lower, {"hello", "hi", "hey"})) {
                responses.push_back("Hi there! How can I help you?");
            }
            // Check for farewells
            else if (containsWord(msg_lower, {"bye", "goodbye", "exit"})) {
                responses.push_back("Goodbye! Have a great day!");
            }
            // Check for weather keywords
            else if (contains(msg_lower, {"weather", "temperature", "forecast"})) {
                responses.push_back("I'm sorry, I can't check the weather, but it's always nice to go outside!");
            }
            // Check for name/identity
            else if (msg_lower.find("name") != string::npos || msg_lower.find("who are you") != string::npos) {
                responses.push_back("I'm a simple chatbot created to assist you.");
            }
            // Check for help keywords
            else if (contains(msg_lower, {"help", "assist", "support"})) {
                responses.push_back("I can chat with you! Try asking about the weather or saying hello.");
            }
            else {
                responses.push_back("I'm not sure I understand. Can you rephrase that?");
            }
        }
        
        return responses;
    }
};

int main() {
    int n;
    cin >> n;
    cin.ignore(); // Ignore newline after n
    
    vector<string> messages;
    for (int i = 0; i < n; i++) {
        string msg;
        getline(cin, msg);
        messages.push_back(msg);
    }
    
    Solution solution;
    vector<string> responses = solution.chatbotResponses(messages);
    
    for (const string& response : responses) {
        cout << response << endl;
    }
    
    return 0;
}
