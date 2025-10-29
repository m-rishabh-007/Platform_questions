using namespace std;
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

class Solution {
public:
    long long minSumOfProducts(vector<int>& A, vector<int>& B) {
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());

        long long min_sum = 0;
        int n = B.size();

        for (int i = 0; i < n; ++i) {
            min_sum += (long long)A[i] * B[n - 1 - i];
        }
        return min_sum;
    }
};

int main() {
    string line;
    
    getline(cin, line);
    istringstream iss1(line);
    vector<int> A;
    int num;
    while (iss1 >> num) {
        A.push_back(num);
    }
    
    getline(cin, line);
    istringstream iss2(line);
    vector<int> B;
    while (iss2 >> num) {
        B.push_back(num);
    }
    
    Solution sol;
    long long result = sol.minSumOfProducts(A, B);
    
    cout << result << endl;
    
    return 0;
}
