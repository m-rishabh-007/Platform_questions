// wrapper.cpp - Execution wrapper for Judge0
// This file handles I/O and executes the contestant's Solution class

#include <iostream>
#include <iomanip>
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
        double principal, rate, time;
        cin >> principal >> rate >> time;
        
        // Create solution instance
        Solution solution;
        
        // Call the solution method
        double result = solution.calculateSimpleInterest(principal, rate, time);
        
        // Print output according to problem specification
        cout << fixed << setprecision(2) << result << endl;
        
    } catch (const exception& e) {
        cerr << "Runtime Error: " << e.what() << endl;
        return 1;
    }
    
    return 0;
}