#include <iostream>
#include <string>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// ===== END INJECTION POINT =====

int main() {
    string name;
    int roll;
    float marks;
    cin >> name >> roll >> marks;
    Solution solution;
    string result = solution.getStudentDetails(name, roll, marks);
    cout << result << endl;
    return 0;
}
