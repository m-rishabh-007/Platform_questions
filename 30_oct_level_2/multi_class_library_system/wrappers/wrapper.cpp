#include <iostream>
#include <vector>
#include <string>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    vector<string> commands;
    string line;
    
    while (getline(cin, line) && line != "EXIT") {
        commands.push_back(line);
    }
    
    Solution sol;
    vector<string> results = sol.processCommands(commands);
    
    for (const string& result : results) {
        cout << result << endl;
    }
    
    return 0;
}
