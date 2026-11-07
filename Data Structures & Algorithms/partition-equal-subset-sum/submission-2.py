class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        def backtrack(i, partial_sum):
            if partial_sum == target:
                return True
            
            if partial_sum > target or i >= len(nums):
                return False
            
            for j in range(i, len(nums)):
                if backtrack(j + 1, partial_sum + nums[j]):
                    return True
            return False
        
        return backtrack(0, 0)
