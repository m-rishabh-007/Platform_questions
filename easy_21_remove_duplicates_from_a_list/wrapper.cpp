// wrapper.cpp - Execution wrapper for Judge0
// This file handles I/O and executes the contestant's Solution class

#include <iostream>
#include <vector>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// Example of what gets injected:
// class Solution {
// public:
//     returnType methodName(paramType param) {
//         return result;
//     }
// };
// ===== END INJECTION POINT =====

int main() {
    try {
        // Read input according to problem specification
        int n;
        cin >> n;
        
        vector<int> numbers(n);
        for (int i = 0; i < n; i++) {
            cin >> numbers[i];
        }
        
        // Create solution instance
        Solution solution;
        
        // Call the solution method
        vector<int> result = solution.removeDuplicates(numbers);
        
        // Print output according to problem specification
        for (size_t i = 0; i < result.size(); i++) {
            cout << result[i];
            if (i < result.size() - 1) cout << " ";
        }
        cout << endl;
        
    } catch (const exception& e) {
        cerr << "Runtime Error: " << e.what() << endl;
        return 1;
    }
    
    return 0;
}