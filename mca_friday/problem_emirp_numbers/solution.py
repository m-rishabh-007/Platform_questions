from typing import TextIO
import sys

class Solution:
    def find_nth_emirp(self, n):
        """
        Find the n-th Emirp number.
        
        :type n: int
        :rtype: int
        """
        def is_prime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True
        
        def reverse_number(num):
            return int(str(num)[::-1])
        
        def is_emirp(num):
            if not is_prime(num):
                return False
            
            reversed_num = reverse_number(num)
            
            # Must be different (not palindrome) and prime
            return reversed_num != num and is_prime(reversed_num)
        
        count = 0
        num = 2
        
        while count < n:
            if is_emirp(num):
                count += 1
                if count == n:
                    return num
            num += 1
        
        return -1

def solve(infile: TextIO = sys.stdin, outfile: TextIO = sys.stdout) -> None:
    n = int(infile.read().strip())
    
    solution = Solution()
    result = solution.find_nth_emirp(n)
    outfile.write(f"{result}\n")

if __name__ == "__main__":
    solve()
