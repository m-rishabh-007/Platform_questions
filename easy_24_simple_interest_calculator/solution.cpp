#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double calculateSimpleInterest(double principal, double rate, double time) {
        return (principal * rate * time) / 100.0;
    }
};

void solve(istream& in = cin, ostream& out = cout) {
    double principal, rate, time;
    in >> principal >> rate >> time;
    
    Solution solution;
    double result = solution.calculateSimpleInterest(principal, rate, time);
    
    out << fixed << setprecision(2) << result << endl;
}

int main() {
    solve();
    return 0;
}
