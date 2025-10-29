#include <iostream>
#include <vector>
#include <string>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

int main() {
    int n, m, t;
    cin >> n >> m >> t;
    cin.ignore();
    
    vector<string> requests;
    for (int i = 0; i < t; i++) {
        string line;
        getline(cin, line);
        requests.push_back(line);
    }
    
    Solution solution;
    vector<string> output = solution.simulateElevatorSystem(n, m, requests);
    
    for (const string& line : output) {
        cout << line << endl;
    }
    
    return 0;
}
