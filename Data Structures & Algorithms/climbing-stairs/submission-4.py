class Solution:
    def climbStairs(self, n: int) -> int:
        # n =4
        #                   *
        #           1              2  
        #       2       3       3       4               (2 jumps)
        #   3    4    4  5    4  5     

        dp = [0 for _ in range(n + 1)]

        dp[n] = 1
        dp[n - 1] = 1

        for i in reversed(range(n - 1)):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]

        # def dfs(total):
        #     nonlocal res
        #     if total == n:
        #         res += 1
        #         return
        #     elif total > n:
        #         return
            
        #     dfs(total + 1)
        #     dfs(total + 2)
        
        # dfs(0)
        # return res
