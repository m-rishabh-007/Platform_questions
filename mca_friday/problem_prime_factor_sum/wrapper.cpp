#include <iostream>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// ===== END INJECTION POINT =====

int main() {
    long long n;
    cin >> n;
    
    Solution solution;
    cout << solution.sum_of_prime_factors(n) << endl;
    
    return 0;
}
