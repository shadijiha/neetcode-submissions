class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Bottom up DP https://youtu.be/Mjy4hd2xgrs?si=CBuWrTb9XyvfRxk2&t=703
        # amount = 4, coins = [1,2,3]
        #           
        #        0     1    2   3   4    <-- amounts
        #  0     0     1    1   1   1
        #  1     0     1    2   2   3                              
        #  2                        
        #   dp[i][j] = dp[i+1][j] + dp[i][curr_amount-coin]
        # ^coin at i
        ROWS, COLS = len(coins), amount + 1
        dp = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            dp[r][0] = 1 # There's only 1 way of getting 0 by selecting a coin (base case)

        for r in reversed(range(ROWS)):
            for c in range(1, COLS):
                coin = coins[r]
                previous_row_value = dp[r+1][c] if r + 1 in range(ROWS) else 0
                same_row_value = dp[r][c - coin] if c - coin in range(COLS) else 0

                dp[r][c] = previous_row_value + same_row_value

        return dp[0][-1]