class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # [3,1,2]
        #
        #
        memo = {}

        def backtrack(index, cumulative):
            cumulative += nums[index]

            if cumulative == target:
                return 1
            if cumulative > target:
                return 0

            if cumulative in memo:
                return memo[cumulative]
            
            total = 0

            for i in range(len(nums)):
                total += backtrack(i, cumulative) 
            
            memo[cumulative] = total
            return total

        grand_total = 0
        for i in range(len(nums)):
            grand_total += backtrack(i, 0)

        return grand_total