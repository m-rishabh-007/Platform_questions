class Solution(object):
    def maxEnergy(self, n, m, h, capacity, power):
        """
        :type n: int
        :type m: int
        :type h: int
        :type capacity: List[int]
        :type power: List[int]
        :rtype: int
        """
        # Sort both arrays in descending order
        capacity.sort(reverse=True)
        power.sort(reverse=True)
        
        total_energy = 0
        pairs = min(n, m)
        
        for i in range(pairs):
            # Energy that can be generated in h hours
            generated_energy = power[i] * h
            # Take minimum of generated and capacity
            total_energy += min(generated_energy, capacity[i])
        
        return total_energy

def solve(infile, outfile):
    """Standalone execution for orchestrator"""
    t = int(infile.readline())
    results = []
    
    for _ in range(t):
        n, m, h = map(int, infile.readline().split())
        capacity = list(map(int, infile.readline().split()))
        power = list(map(int, infile.readline().split()))
        
        solution = Solution()
        result = solution.maxEnergy(n, m, h, capacity, power)
        results.append(result)
    
    for r in results:
        outfile.write(str(r) + '\n')

if __name__ == "__main__":
    import sys
    solve(sys.stdin, sys.stdout)

