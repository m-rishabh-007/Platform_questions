#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> analyze_sort_performance(const vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) {
            return {0, 0};
        }
        
        // Calculate naive bubble sort metrics
        int naive_comparisons = 0;
        for (int i = 0; i < n - 1; i++) {
            naive_comparisons += (n - 1 - i);
        }
        
        vector<int> arr_copy = arr;
        int naive_swaps = count_naive_swaps(arr_copy);
        
        // Calculate optimized bubble sort metrics
        arr_copy = arr;
        auto optimized_metrics = count_optimized_metrics(arr_copy);
        int optimized_comparisons = optimized_metrics.first;
        int optimized_swaps = optimized_metrics.second;
        
        int comparison_savings = naive_comparisons - optimized_comparisons;
        int swap_savings = naive_swaps - optimized_swaps;
        
        return {comparison_savings, swap_savings};
    }

private:
    int count_naive_swaps(vector<int>& arr) {
        int n = arr.size();
        int swap_count = 0;
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                    swap_count++;
                }
            }
        }
        
        return swap_count;
    }
    
    pair<int, int> count_optimized_metrics(vector<int>& arr) {
        int n = arr.size();
        int comparison_count = 0;
        int swap_count = 0;
        int boundary = n - 1;
        
        while (boundary > 0) {
            int last_swap_index = -1;
            int current_comparisons = 0;
            int current_swaps = 0;
            
            // Perform comparisons up to the boundary
            for (int j = 0; j < boundary; j++) {
                current_comparisons++;
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                    current_swaps++;
                    last_swap_index = j;
                }
            }
            
            comparison_count += current_comparisons;
            swap_count += current_swaps;
            
            // Early termination if no swaps occurred
            if (current_swaps == 0) {
                break;
            }
            
            // Update boundary to last swap position
            boundary = last_swap_index;
        }
        
        return {comparison_count, swap_count};
    }
};

void solve(istream& in = cin, ostream& out = cout) {
    int n;
    in >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        in >> arr[i];
    }
    
    Solution solution;
    auto result = solution.analyze_sort_performance(arr);
    
    out << result[0] << " " << result[1] << "\n";
}

int main() {
    solve();
    return 0;
}