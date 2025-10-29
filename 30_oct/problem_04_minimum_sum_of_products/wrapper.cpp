#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

void readVector(vector<int>& vec) {
    string line;
    getline(cin, line);
    stringstream ss(line);
    int num;
    while (ss >> num) {
        vec.push_back(num);
    }
}

int main() {
    vector<int> A, B;
    readVector(A);
    readVector(B);
    
    Solution sol;
    cout << sol.minSumOfProducts(A, B) << endl;
    
    return 0;
}
