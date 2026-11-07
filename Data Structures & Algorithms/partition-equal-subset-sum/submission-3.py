class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        memo = {}
        def backtrack(i, partial_sum):
            if partial_sum == target:
                return True
            
            if partial_sum > target or i >= len(nums):
                return False

            if (i, partial_sum) in memo:
                return memo[(i, partial_sum)]
            
            for j in range(i, len(nums)):
                if backtrack(j + 1, partial_sum + nums[j]):
                    memo[(j + 1, partial_sum + nums[j])] = True
                    return True
                
            memo[(i, partial_sum)] = False
            return False
        
        return backtrack(0, 0)
