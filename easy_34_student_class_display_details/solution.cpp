using namespace std;
#include <iostream>
#include <string>

class Solution {
public:
    string getStudentDetails(const string& name, int roll, float marks) {
        return "Name: " + name + ", Roll: " + to_string(roll) + ", Marks: " + to_string(marks);
    }
};

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