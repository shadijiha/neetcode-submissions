class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        grand_total = 0
        subset = 0

        def backtrack(start):
            nonlocal subset, grand_total
            grand_total += subset
            
            for i in range(start, len(nums)):
                subset = subset ^ nums[i]
                backtrack(i + 1)
                subset = subset ^ nums[i]

        backtrack(0)
        return grand_total
