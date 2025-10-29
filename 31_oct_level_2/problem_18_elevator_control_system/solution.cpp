#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <sstream>
#include <cmath>
#include <climits>
using namespace std;

class Solution {
private:
    enum Direction { IDLE, UP, DOWN };
    enum State { STOPPED, MOVING, DOORS_OPEN };
    
    struct Elevator {
        int id;
        int currentFloor;
        Direction direction;
        State state;
        queue<int> destinations;
        bool busy;
        
        Elevator(int id) : id(id), currentFloor(1), direction(IDLE), state(STOPPED), busy(false) {}
    };
    
public:
    vector<string> simulateElevatorSystem(int numFloors, int numElevators, 
                                          vector<string>& requests) {
        vector<Elevator> elevators;
        for (int i = 0; i < numElevators; i++) {
            elevators.push_back(Elevator(i));
        }
        
        vector<string> output;
        int step = 0;
        
        for (const string& req : requests) {
            istringstream iss(req);
            string type;
            iss >> type;
            
            if (type == "EXTERNAL") {
                int floor;
                string dir;
                iss >> floor >> dir;
                
                // Simple dispatch: find nearest idle elevator
                int bestElev = -1;
                int minDist = INT_MAX;
                
                for (int i = 0; i < numElevators; i++) {
                    if (!elevators[i].busy) {
                        int dist = abs(elevators[i].currentFloor - floor);
                        if (dist < minDist) {
                            minDist = dist;
                            bestElev = i;
                        }
                    }
                }
                
                // If no idle elevator, use first one
                if (bestElev == -1) {
                    bestElev = 0;
                }
                
                elevators[bestElev].destinations.push(floor);
                elevators[bestElev].busy = true;
                output.push_back("Step " + to_string(step) + 
                               ": Elevator " + to_string(bestElev) + 
                               " dispatched to floor " + to_string(floor));
            }
            else if (type == "INTERNAL") {
                int elevId, dest;
                iss >> elevId >> dest;
                
                if (elevId >= 0 && elevId < numElevators) {
                    elevators[elevId].destinations.push(dest);
                    elevators[elevId].busy = true;
                    output.push_back("Step " + to_string(step) + 
                                   ": Elevator " + to_string(elevId) + 
                                   " moving to floor " + to_string(dest));
                }
            }
            
            step++;
        }
        
        return output;
    }
};

void solve() {
    int n, m, t;
    cin >> n >> m >> t;
    cin.ignore();
    
    vector<string> requests;
    for (int i = 0; i < t; i++) {
        string line;
        getline(cin, line);
        requests.push_back(line);
    }
    
    Solution solution;
    vector<string> output = solution.simulateElevatorSystem(n, m, requests);
    
    for (const string& line : output) {
        cout << line << endl;
    }
}

int main() {
    solve();
    return 0;
}
