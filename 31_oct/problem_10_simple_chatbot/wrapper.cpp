#include <iostream>
#include <vector>
#include <string>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int n;
    cin >> n;
    cin.ignore();
    
    vector<string> messages;
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        messages.push_back(line);
    }
    
    Solution solution;
    vector<string> responses = solution.chatbotResponses(messages);
    
    for (const string& response : responses) {
        cout << response << endl;
    }
    
    return 0;
}
