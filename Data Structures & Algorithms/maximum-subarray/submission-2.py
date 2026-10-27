class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #
        # [2,-3,4,-2,2,1,-1,4]
        #       ^           ^
        # [999,-3,4,9,2,1,9,4]
        result = -math.inf

        l, r = 0, 0

        currentTotal = 0
        while r < len(nums):
            currentTotal += nums[r]
            result = max(result, currentTotal)

            while l <= r and currentTotal < 0:
                currentTotal -= nums[l]
                l += 1
            r += 1
        
        return result