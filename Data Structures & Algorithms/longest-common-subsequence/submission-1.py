class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #
        # t1 = cat
        # t2 = crabt
        # 
        # dp=
        rows, cols = len(text2), len(text1)
        dp = [ [0] * (cols + 1) for _ in range(rows+1) ] 

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if text2[r] == text1[c]:
                    # Char is matched, advance both indices (substring)
                    subproblem = dp[r+1][c+1]
                    dp[r][c] = 1 + subproblem
                else:
                    # Get the max between advancing 1 of the indicies
                    advanceText1 = dp[r][c+1]
                    advanceText2 = dp[r+1][c]
                    dp[r][c] = max(advanceText1, advanceText2)

        return dp[0][0]