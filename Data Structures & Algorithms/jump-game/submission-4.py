class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #   [1,2,0,1,0]
        #          ^
        #dp=[T T F T T]

        dp = [False] * len(nums)
        dp[-1] = True

        for i in reversed(range(len(nums) - 1)):
            jumpCount = nums[i]
            canReach = False
            for j in range(i+1, i+jumpCount+1):
                canReach = canReach or dp[j]
            dp[i] = canReach
        
        return dp[0]
        
