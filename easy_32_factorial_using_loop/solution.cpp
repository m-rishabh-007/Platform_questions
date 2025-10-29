#include <iostream>
using namespace std;

class Solution {
public:
    int computeFactorial(int n) {
        int result = 1;
        for (int i = 2; i <= n; ++i) {
            result *= i;
        }
        return result;
    }
};

int main() {
    int n;
    cin >> n;
    Solution solution;
    int result = solution.computeFactorial(n);
    cout << result << endl;
    return 0;
}