#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }
};

void solve(istream& in = cin, ostream& out = cout) {
    int year;
    in >> year;
    
    Solution solution;
    bool result = solution.isLeapYear(year);
    
    out << (result ? "True" : "False") << endl;
}

int main() {
    solve();
    return 0;
}
