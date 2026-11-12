class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
      #
      #       1     2   3   1
      #. 1                  1
      #. 2                  0
      #  3                  2
      #  1              2   1
      #                     
      #
      # let dp[i][j] be the score difference between 2 player
      # dp[i][j] = piles[i] - dp[i + 1][j]
      # dp[i][j] = piles[j] - dp[i][j + 1]
      # max ^
      # base case = dp[-1][-1] = piles[-1]
        N = len(piles)
        dp = [([0] * N) for _ in range(N)]
       
        # Base cases
        for i in range(N):
            dp[i][i] = piles[i]

        for i in reversed(range(N)):
            for j in range(N):
                right = piles[i] - (dp[i + 1][j] if i + 1 < N else 0)
                bottom = piles[j] - (dp[i][j - 1] if j - 1 >= 0 else 0)
                dp[i][j] = max(right, bottom)
        
        return dp[0][0] > 0