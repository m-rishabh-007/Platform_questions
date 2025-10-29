#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

class Solution {
private:
    struct Appointment {
        int id;
        string date;
        string time;
        string description;
    };
    
    vector<Appointment> appointments;
    int nextId = 1;
    
public:
    vector<string> processOperations(vector<string>& operations) {
        vector<string> results;
        
        for (const string& op : operations) {
            if (op.substr(0, 3) == "ADD") {
                // Parse: ADD YYYY-MM-DD HH:MM description
                size_t pos1 = 4;
                size_t pos2 = op.find(' ', pos1);
                string date = op.substr(pos1, pos2 - pos1);
                
                size_t pos3 = pos2 + 1;
                size_t pos4 = op.find(' ', pos3);
                string time = op.substr(pos3, pos4 - pos3);
                
                string description = op.substr(pos4 + 1);
                
                Appointment apt = {nextId, date, time, description};
                appointments.push_back(apt);
                
                results.push_back("Added appointment #" + to_string(nextId) + 
                                ": " + description + " at " + date + " " + time);
                nextId++;
            }
            else if (op.substr(0, 4) == "LIST") {
                string date = op.substr(5);
                vector<string> dateAppointments;
                
                for (const auto& apt : appointments) {
                    if (apt.date == date) {
                        dateAppointments.push_back(to_string(apt.id) + ". " + 
                                                  apt.time + " - " + apt.description);
                    }
                }
                
                if (dateAppointments.empty()) {
                    results.push_back("No appointments for " + date);
                } else {
                    for (const string& s : dateAppointments) {
                        results.push_back(s);
                    }
                }
            }
            else if (op.substr(0, 6) == "DELETE") {
                int id = stoi(op.substr(7));
                bool found = false;
                
                for (auto it = appointments.begin(); it != appointments.end(); ++it) {
                    if (it->id == id) {
                        appointments.erase(it);
                        found = true;
                        break;
                    }
                }
                
                if (found) {
                    results.push_back("Deleted appointment #" + to_string(id));
                } else {
                    results.push_back("Appointment #" + to_string(id) + " not found");
                }
            }
        }
        
        return results;
    }
};

int main() {
    int n;
    cin >> n;
    cin.ignore();
    
    vector<string> operations;
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        operations.push_back(line);
    }
    
    Solution solution;
    vector<string> results = solution.processOperations(operations);
    
    for (const string& result : results) {
        cout << result << endl;
    }
    
    return 0;
}
