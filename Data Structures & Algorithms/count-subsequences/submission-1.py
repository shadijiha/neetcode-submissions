class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #
        #                       *
        #              c
        #        a          a
        #    t          a
        #
        #       c   a   a   a   t
        #.  c                       0
        #   a                       0
        #   t                       0
        #       1   1   1   1   1   1                
        # if s[i] == t[j] --> dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
        # else: dp[i][j] = dp[i + 1][j]
        ROWS, COLS = len(t), len(s)

        dp = [([0] * (COLS+1)) for _ in range(ROWS+1)]

        for c in range(COLS + 1):
            dp[ROWS][c] = 1
        
        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                if t[r] == s[c]:
                    dp[r][c] = dp[r + 1][c + 1] + dp[r][c + 1]
                else:
                    dp[r][c] = dp[r][c + 1]
        
        return dp[0][0]