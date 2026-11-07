class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num = nums[0]
        for i in range(1, len(nums)):
            num = num ^ nums[i]

        return num