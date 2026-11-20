class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[s] = number of ways to reach the target starting from sum s
        dp = [0] * (target + 1)
        dp[target] = 1

        for s in reversed(range(target)):
            for n in nums:
                if s + n > target:
                    continue
                
                dp[s] += dp[n + s]

        return dp[0]
