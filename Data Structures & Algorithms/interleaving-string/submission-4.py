class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # ? = out of bounds
        #  aabbbbaa
        #       a   a   a   a   ?
        #  b                   
        #  b                   
        #  b                   
        #  b                   
        #  ?                    T
        #  dp[i][j] = dp[i+1][j] OR dp[i][j+1]
        # if we reach out of bound on both string = True we found a solution
        ROWS, COLS = len(s1), len(s2)

        if ROWS + COLS != len(s3):
            return False

        dp = [ ( [False] * (COLS+1) ) for _ in range(ROWS+1)]
        dp[-1][-1] = True

        for r in reversed(range(ROWS+1)):
            for c in reversed(range(COLS+1)):
                char_1 = s1[r] if r < len(s1) else ""
                char_2 = s2[c] if c < len(s2) else ""

                if r + c >= len(s3): continue
                char_3 = s3[r+c]

                if char_1 == char_3:
                    dp[r][c] = dp[r+1][c]
                if char_2 == char_3:
                    dp[r][c] = dp[r][c+1]

        
        return dp[0][0]