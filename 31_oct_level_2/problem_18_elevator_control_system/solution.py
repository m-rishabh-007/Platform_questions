from typing import TextIO, List
import sys
from collections import deque

class Solution(object):
    def simulateElevatorSystem(self, numFloors, numElevators, requests):
        """
        :type numFloors: int
        :type numElevators: int
        :type requests: List[str]
        :rtype: List[str]
        """
        class Elevator:
            def __init__(self, elevator_id):
                self.id = elevator_id
                self.current_floor = 1
                self.direction = "IDLE"
                self.state = "IDLE"
                self.destinations = deque()
                self.busy = False
        
        elevators = [Elevator(i) for i in range(numElevators)]
        output = []
        step = 0
        
        for req in requests:
            parts = req.split()
            req_type = parts[0]
            
            if req_type == "EXTERNAL":
                floor = int(parts[1])
                direction = parts[2]
                
                # Simple dispatch: find nearest idle elevator
                best_elev = -1
                min_dist = float('inf')
                
                for i in range(numElevators):
                    if not elevators[i].busy:
                        dist = abs(elevators[i].current_floor - floor)
                        if dist < min_dist:
                            min_dist = dist
                            best_elev = i
                
                # If no idle elevator, use first one
                if best_elev == -1:
                    best_elev = 0
                
                elevators[best_elev].destinations.append(floor)
                elevators[best_elev].busy = True
                output.append(f"Step {step}: Elevator {best_elev} dispatched to floor {floor}")
                
            elif req_type == "INTERNAL":
                elev_id = int(parts[1])
                dest = int(parts[2])
                
                if 0 <= elev_id < numElevators:
                    elevators[elev_id].destinations.append(dest)
                    elevators[elev_id].busy = True
                    output.append(f"Step {step}: Elevator {elev_id} moving to floor {dest}")
            
            step += 1
        
        return output

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n, m, t = map(int, infile.readline().split())
    requests = []
    for _ in range(t):
        requests.append(infile.readline().strip())
    
    solution = Solution()
    output = solution.simulateElevatorSystem(n, m, requests)
    
    for line in output:
        outfile.write(line + '\n')

if __name__ == "__main__":
    solve()
