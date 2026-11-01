class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #  https://www.youtube.com/watch?v=XYi2-LPrwm4
        #               m   o   n   k   e   y   s
        #   m
        #   o
        #   n
        #   e
        #   y
        ROWS, COLS = len(word1), len(word2)
        if ROWS == 0 or COLS == 0:
            return max(ROWS, COLS)

        dp = [[0] * (COLS+1) for _ in range(ROWS+1)]

        for r in range(ROWS):
            dp[r][-1] = len(word1) - r
        
        for c in range(COLS):
            dp[-1][c] = len(word2) - c

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                char1, char2 = word1[r], word2[c]

                if char1 == char2:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    replace = dp[r+1][c+1]
                    remove = dp[r+1][c]
                    insert = dp[r][c+1]

                    dp[r][c] = 1 + min(replace, remove, insert)
        print(dp)
        return dp[0][0]