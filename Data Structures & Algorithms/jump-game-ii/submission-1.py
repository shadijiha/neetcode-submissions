class Solution:
    def jump(self, nums: List[int]) -> int:
        #
        #   [2,4,1,1,1,1]
        #    
        # dp[2 1 3 2 1 0]
        if len(nums) <= 0:
            return 0
        
        dp = [math.inf] * len(nums)
        dp[-1] = 0

        for i in reversed(range(len(nums) - 1)):
            jumpDistance = nums[i]
            if jumpDistance == 0: continue
            dp[i] = 1 + min(dp[i+1:i+jumpDistance+1])
        
        return dp[0]