class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # let dp[i][j] = how much Champagne  reached
        GLASSES = 100
        dp = [[0.0] * (GLASSES+1) for _ in range(GLASSES+1)]
        dp[0][0] = poured
        
        for i in range(GLASSES):
            for j in range(i+1):  # because row i has i + 1 glasses
                if dp[i][j] > 1:
                    CUP_CAPACITY = 1
                    overflow = (dp[i][j] - CUP_CAPACITY) / 2

                    dp[i + 1][j] += overflow
                    dp[i + 1][j + 1] += overflow
        
        return min(1.0, dp[query_row][query_glass])

