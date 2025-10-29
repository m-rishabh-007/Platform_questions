#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> find_emirps_in_range(int limit) {
        if (limit < 13) {  // Smallest Emirp is 13
            return {};
        }
        
        // Generate all primes up to limit using Sieve of Eratosthenes
        vector<int> primes = sieve_of_eratosthenes(limit);
        
        vector<int> emirps;
        
        for (int prime : primes) {
            if (prime < 10) {  // Skip single-digit primes
                continue;
            }
            
            // Reverse the digits
            int reversed_num = reverse_digits(prime);
            
            // Check if the reversed number is different and also prime
            if (reversed_num != prime && is_prime(reversed_num)) {
                emirps.push_back(prime);
            }
        }
        
        sort(emirps.begin(), emirps.end());
        return emirps;
    }

private:
    vector<int> sieve_of_eratosthenes(int n) {
        if (n < 2) {
            return {};
        }
        
        // Create a boolean array and initialize all entries as True
        vector<bool> is_prime(n + 1, true);
        is_prime[0] = is_prime[1] = false;
        
        for (int p = 2; p * p <= n; p++) {
            if (is_prime[p]) {
                // Update all multiples of p
                for (int i = p * p; i <= n; i += p) {
                    is_prime[i] = false;
                }
            }
        }
        
        // Collect all prime numbers
        vector<int> primes;
        for (int i = 2; i <= n; i++) {
            if (is_prime[i]) {
                primes.push_back(i);
            }
        }
        
        return primes;
    }
    
    bool is_prime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        
        // Check odd divisors up to sqrt(n)
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
    
    int reverse_digits(int num) {
        int reversed = 0;
        while (num > 0) {
            reversed = reversed * 10 + num % 10;
            num /= 10;
        }
        return reversed;
    }
};

void solve(istream& in = cin, ostream& out = cout) {
    int limit;
    in >> limit;
    
    Solution solution;
    auto result = solution.find_emirps_in_range(limit);
    
    if (!result.empty()) {
        for (size_t i = 0; i < result.size(); i++) {
            out << result[i];
            if (i + 1 < result.size()) {
                out << " ";
            }
        }
    }
    out << "\n";
}

int main() {
    solve();
    return 0;
}