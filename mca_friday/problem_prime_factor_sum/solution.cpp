#include <iostream>
using namespace std;

class Solution {
public:
    long long sum_of_prime_factors(long long n) {
        long long sum = 0;
        
        // Check for factor 2
        if (n % 2 == 0) {
            sum += 2;
            while (n % 2 == 0) {
                n /= 2;
            }
        }
        
        // Check for odd factors from 3 onwards
        for (long long i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                sum += i;
                while (n % i == 0) {
                    n /= i;
                }
            }
        }
        
        // If n is still greater than 1, then it's a prime factor
        if (n > 1) {
            sum += n;
        }
        
        return sum;
    }
};

int main() {
    long long n;
    cin >> n;
    
    Solution solution;
    cout << solution.sum_of_prime_factors(n) << endl;
    
    return 0;
}
