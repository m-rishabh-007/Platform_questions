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
    
    vector<string> operations;
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        operations.push_back(line);
    }
    
    Solution solution;
    vector<string> results = solution.processOperations(operations);
    
    for (const string& result : results) {
        cout << result << endl;
    }
    
    return 0;
}
