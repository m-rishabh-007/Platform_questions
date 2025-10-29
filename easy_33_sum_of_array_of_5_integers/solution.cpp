using namespace std;
#include <vector>
#include <iostream>

class Solution {
public:
    int sumOfFive(const std::vector<int>& arr) {
        int total = 0;
        for (int x : arr) total += x;
        return total;
    }
};

int main() {
    std::vector<int> arr(5);
    for (int i = 0; i < 5; ++i) {
        std::cin >> arr[i];
    }
    Solution solution;
    int result = solution.sumOfFive(arr);
    std::cout << result << std::endl;
    return 0;
}