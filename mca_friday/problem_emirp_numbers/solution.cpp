#include <iostream>
using namespace std;

class Solution {
private:
    bool isPrime(int num) {
        if (num < 2) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;
        
        for (int i = 3; i * i <= num; i += 2) {
            if (num % i == 0) return false;
        }
        return true;
    }
    
    int reverseNumber(int num) {
        int reversed = 0;
        while (num > 0) {
            reversed = reversed * 10 + num % 10;
            num /= 10;
        }
        return reversed;
    }
    
    bool isEmirp(int num) {
        if (!isPrime(num)) return false;
        
        int reversed = reverseNumber(num);
        
        // Must be different (not palindrome) and prime
        return reversed != num && isPrime(reversed);
    }
    
public:
    int find_nth_emirp(int n) {
        int count = 0;
        int num = 2;
        
        while (count < n) {
            if (isEmirp(num)) {
                count++;
                if (count == n) {
                    return num;
                }
            }
            num++;
        }
        
        return -1;
    }
};

int main() {
    int n;
    cin >> n;
    
    Solution solution;
    cout << solution.find_nth_emirp(n) << endl;
    
    return 0;
}
