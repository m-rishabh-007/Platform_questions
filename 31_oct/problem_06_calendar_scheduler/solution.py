import sys
from typing import TextIO

class Solution(object):
    def __init__(self):
        self.appointments = []
        self.next_id = 1
    
    def processOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: List[str]
        """
        results = []
        
        for op in operations:
            if op.startswith("ADD"):
                # Parse: ADD YYYY-MM-DD HH:MM description
                parts = op.split(' ', 3)
                date = parts[1]
                time = parts[2]
                description = parts[3]
                
                appointment = {
                    'id': self.next_id,
                    'date': date,
                    'time': time,
                    'description': description
                }
                self.appointments.append(appointment)
                
                results.append(f"Added appointment #{self.next_id}: {description} at {date} {time}")
                self.next_id += 1
                
            elif op.startswith("LIST"):
                date = op.split(' ', 1)[1]
                date_appointments = [apt for apt in self.appointments if apt['date'] == date]
                
                if not date_appointments:
                    results.append(f"No appointments for {date}")
                else:
                    for apt in date_appointments:
                        results.append(f"{apt['id']}. {apt['time']} - {apt['description']}")
                        
            elif op.startswith("DELETE"):
                apt_id = int(op.split(' ', 1)[1])
                found = False
                
                for i, apt in enumerate(self.appointments):
                    if apt['id'] == apt_id:
                        self.appointments.pop(i)
                        found = True
                        break
                
                if found:
                    results.append(f"Deleted appointment #{apt_id}")
                else:
                    results.append(f"Appointment #{apt_id} not found")
        
        return results

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    """For orchestrator.py execution"""
    n = int(infile.readline())
    operations = []
    for _ in range(n):
        operations.append(infile.readline().strip())
    
    solution = Solution()
    results = solution.processOperations(operations)
    
    for result in results:
        outfile.write(result + '\n')

if __name__ == "__main__":
    solve()
