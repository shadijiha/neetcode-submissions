class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        dp[-1] = 1

        for i in reversed(range(len(nums) - 1)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

        # n = len(nums)
        # dp = [0] * (n + 1)
        # dp[n] = 0
        # dp[n - 1] = 1
        # smallestInSeq = nums[-1]

        # for i in reversed(range(n - 1)):
        #     if nums[i] < smallestInSeq:
        #         dp[i] = dp[i + 1] + 1
        #         smallestInSeq = nums[i]
        #     else:
        #         dp[i] = dp[i + 1]
        # return dp[0]