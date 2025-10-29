#include <iostream>
#include <vector>
#include <string>
#include <tuple>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// Contestant's Solution class will be injected here
// ===== END INJECTION POINT =====

int main() {
    // Read inventory data
    int n;
    cin >> n;
    vector<tuple<string, int, int>> inventory_data;
    for (int i = 0; i < n; i++) {
        string name;
        int price, quantity;
        cin >> name >> price >> quantity;
        inventory_data.push_back(make_tuple(name, price, quantity));
    }
    
    // Read purchase requests
    int m;
    cin >> m;
    vector<tuple<string, int>> purchase_requests;
    for (int i = 0; i < m; i++) {
        string product_name;
        int money_inserted;
        cin >> product_name >> money_inserted;
        purchase_requests.push_back(make_tuple(product_name, money_inserted));
    }
    
    // Execute solution
    Solution solution;
    vector<tuple<string, string, int>> results = solution.purchase(inventory_data, purchase_requests);
    
    // Output results
    for (auto& result : results) {
        string status = get<0>(result);
        string item_name = get<1>(result);
        int change = get<2>(result);
        
        if (status == "SUCCESS") {
            cout << status << " " << item_name << " " << change << endl;
        } else {
            cout << status << " " << change << endl;
        }
    }
    
    return 0;
}