class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        increase, decrease = deque(), deque()

        l, r = 0, 0
        result = 1
        while r < len(nums):

            val = nums[r]
            if decrease and val >= nums[decrease[-1]]:
                result = max(result, len(decrease))
                decrease.clear()
                l = r
            decrease.append(r)

            if increase and val <= nums[increase[-1]]:
                result = max(result, len(increase))
                increase.clear()
                l = r
            increase.append(r)

            r += 1
        result = max(result, len(increase), len(decrease))
        return result