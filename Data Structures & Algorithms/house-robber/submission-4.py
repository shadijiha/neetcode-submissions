class Solution:
    def rob(self, nums: List[int]) -> int:
        HOUSES = len(nums)
        if HOUSES == 1:
            return nums[0]
        
        dp = [0 for _ in range(HOUSES + 1)]

        dp[HOUSES] = 0
        dp[HOUSES - 1] = nums[-1]

        for i in reversed(range(HOUSES - 1)):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]
        


        # for i, n in enumerate(nums):
        #     if i == 0:
        #         robArray[i] = n
        #         continue
        #     elif i == 1:
        #         robArray[i] = max(robArray[0], n)
        #         continue

        #     maxRob = max(n + robArray[i - 2], robArray[i - 1])
        #     robArray[i] = maxRob
        
        # return robArray[-1]