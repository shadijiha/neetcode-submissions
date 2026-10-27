class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        COSTS = len(cost)
        dp = [math.inf for _ in range(COSTS + 1)]

        dp[COSTS] = 0
        dp[COSTS - 1] = cost[COSTS - 1]

        for i in reversed(range(COSTS - 1)): 
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])
