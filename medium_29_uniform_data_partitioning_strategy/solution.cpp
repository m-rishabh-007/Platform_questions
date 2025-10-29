#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> calculate_partition_plan(const vector<int>& data_volumes) {
        if (data_volumes.empty()) {
            return {0, 0};
        }
        
        // Calculate GCD of all volumes
        int partition_size = data_volumes[0];
        for (size_t i = 1; i < data_volumes.size(); i++) {
            partition_size = gcd(partition_size, data_volumes[i]);
        }
        
        // Calculate total partitions needed
        int total_partitions = 0;
        for (int volume : data_volumes) {
            total_partitions += volume / partition_size;
        }
        
        return {partition_size, total_partitions};
    }

private:
    int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
};

void solve(istream& in = cin, ostream& out = cout) {
    int n;
    in >> n;
    
    vector<int> data_volumes(n);
    for (int i = 0; i < n; i++) {
        in >> data_volumes[i];
    }
    
    Solution solution;
    auto result = solution.calculate_partition_plan(data_volumes);
    
    out << result[0] << " " << result[1] << "\n";
}

int main() {
    solve();
    return 0;
}