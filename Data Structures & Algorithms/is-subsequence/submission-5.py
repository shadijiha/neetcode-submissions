class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #
        # 
        #
        #
        #
        if not s:
            return True
        if len(s) > len(t):
            return False
        j = 0
        res = 0

        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                res += 1
                j += 1
        
        return res == len(s)
        
        # ROWS, COLS = len(s), len(t)
        # dp = [([False] * COLS) for _ in range(ROWS)]

        # for r in reversed(range(ROWS)):
        #     for c in reversed(range(COLS)):
        #         if s[r] == t[c]:
        #             dp[r][c] = True
        #         else:
        #             right = dp[r][c + 1] if c + 1 < COLS else False
        #             bottom = dp[r + 1][c] if r + 1 < ROWS else False
        #             dp[r][c] = right or bottom
        
        # return dp[0][0]