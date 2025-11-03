#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    int naiveBubbleSort(vector<int> arr) {
        int n = arr.size();
        int comparisons = 0;
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                comparisons++;
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                }
            }
        }
        return comparisons;
    }
    
    int optimizedBubbleSort(vector<int> arr) {
        int n = arr.size();
        int comparisons = 0;
        int lastSwapIndex = n - 1;
        
        while (lastSwapIndex > 0) {
            int newLastSwapIndex = 0;
            
            for (int j = 0; j < lastSwapIndex; j++) {
                comparisons++;
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                    newLastSwapIndex = j;
                }
            }
            
            lastSwapIndex = newLastSwapIndex;
        }
        
        return comparisons;
    }
    
public:
    int calculate_comparison_savings(vector<int>& arr) {
        if (arr.size() <= 1) return 0;
        
        int naiveComparisons = naiveBubbleSort(arr);
        int optimizedComparisons = optimizedBubbleSort(arr);
        
        return naiveComparisons - optimizedComparisons;
    }
};

int main() {
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    Solution solution;
    cout << solution.calculate_comparison_savings(arr) << endl;
    
    return 0;
}
