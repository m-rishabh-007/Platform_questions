class Solution {
public:
    std::string computeFactorial(int n) {
        // Choose approach: recursive or iterative
        // Uncomment one of the following lines as needed:
        // BigInt res = factorial_recursive(n);
        BigInt res = factorial_iterative(n);
        std::ostringstream oss;
        oss << res;
        return oss.str();
    }
};
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>

class BigInt {
public:
    std::vector<int> digits;
    static const int BASE = 10000;
    static const int WIDTH = 4;

    BigInt(int num = 0) { *this = num; }
    BigInt& operator=(int num) {
        digits.clear();
        do {
            digits.push_back(num % BASE);
            num /= BASE;
        } while (num > 0);
        return *this;
    }
    BigInt operator*(int num) const {
        BigInt res;
        res.digits.resize(digits.size() + 10, 0);
        int carry = 0;
        for (size_t i = 0; i < digits.size(); ++i) {
            long long tmp = (long long)digits[i] * num + carry;
            res.digits[i] = tmp % BASE;
            carry = tmp / BASE;
        }
        size_t i = digits.size();
        while (carry) {
            res.digits[i++] = carry % BASE;
            carry /= BASE;
        }
        while (res.digits.size() > 1 && res.digits.back() == 0) res.digits.pop_back();
        return res;
    }
    BigInt& operator*=(int num) { *this = *this * num; return *this; }
    friend std::ostream& operator<<(std::ostream& os, const BigInt& b) {
        os << b.digits.back();
        for (int i = (int)b.digits.size() - 2; i >= 0; --i)
            os << std::setw(WIDTH) << std::setfill('0') << b.digits[i];
        return os;
    }
};

class Solution {
    BigInt factorial(int n) {
        BigInt res(1);
        for (int i = 2; i <= n; ++i) res *= i;
        return res;
    }
public:
    std::string computeFactorial(int n) {
        BigInt res = factorial(n);
        std::ostringstream oss;
        oss << res;
        return oss.str();
    }
};