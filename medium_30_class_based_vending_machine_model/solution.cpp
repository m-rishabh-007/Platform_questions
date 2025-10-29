#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <tuple>
using namespace std;

class Product {
public:
    string name;
    int price;
    
    Product() : name(""), price(0) {}
    Product(string name, int price) : name(name), price(price) {}
};

class VendingMachine {
public:
    map<string, pair<Product, int>> inventory;
    
    VendingMachine() {}
    
    void restock(vector<tuple<string, int, int>>& products) {
        for (auto& item : products) {
            string name = get<0>(item);
            int price = get<1>(item);
            int quantity = get<2>(item);
            
            if (inventory.find(name) != inventory.end()) {
                // Update existing product quantity
                inventory[name].second += quantity;
            } else {
                // Add new product
                inventory[name] = make_pair(Product(name, price), quantity);
            }
        }
    }
};

class Solution {
public:
    vector<tuple<string, string, int>> purchase(vector<tuple<string, int, int>>& inventory_data, 
                                                vector<tuple<string, int>>& purchase_requests) {
        // Initialize vending machine and restock
        VendingMachine machine;
        machine.restock(inventory_data);
        
        vector<tuple<string, string, int>> results;
        
        for (auto& request : purchase_requests) {
            string product_name = get<0>(request);
            int money_inserted = get<1>(request);
            
            // Check if product exists
            if (machine.inventory.find(product_name) == machine.inventory.end()) {
                results.push_back(make_tuple("PRODUCT_NOT_FOUND", "", money_inserted));
                continue;
            }
            
            // Check if product is available
            if (machine.inventory[product_name].second <= 0) {
                results.push_back(make_tuple("OUT_OF_STOCK", "", money_inserted));
                continue;
            }
            
            // Check if sufficient money provided
            int product_price = machine.inventory[product_name].first.price;
            if (money_inserted < product_price) {
                results.push_back(make_tuple("INSUFFICIENT_FUNDS", "", money_inserted));
                continue;
            }
            
            // Process successful purchase
            int change = money_inserted - product_price;
            machine.inventory[product_name].second--;
            results.push_back(make_tuple("SUCCESS", product_name, change));
        }
        
        return results;
    }
};

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