import sys

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # dp[i][j] = True if s[0..i-1] matches p[0..j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like *, **, ***, etc. at the beginning
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    # * can match empty sequence or one/more characters
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    # ? matches any single char, or exact character match
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[m][n]

def solve(infile, outfile):
    """Standalone execution for orchestrator"""
    s = infile.readline().strip()
    p = infile.readline().strip()
    
    solution = Solution()
    result = solution.isMatch(s, p)
    outfile.write("true\n" if result else "false\n")

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
