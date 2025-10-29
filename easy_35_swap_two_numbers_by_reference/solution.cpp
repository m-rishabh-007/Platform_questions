using namespace std;
#include <iostream>

class Solution {
public:
    void swapNumbers(int &a, int &b) {
        int temp = a;
        a = b;
        b = temp;
    }
};

int main() {
    int a, b;
    cin >> a >> b;
    Solution solution;
    solution.swapNumbers(a, b);
    cout << a << " " << b << endl;
    return 0;
}