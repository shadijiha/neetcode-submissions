class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [0 for _ in nums]
        prefix = [0 for _ in nums]
        postfix = [0 for _ in nums]

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]
        
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i + 1]
       
        for i in range(len(nums) - 1):
            if i == 0:
                result[i] = postfix[i + 1]
                continue
            
            result[i] = prefix[i - 1] * postfix[i + 1]

        result[len(nums) - 1] = prefix[len(nums) - 2]

        return result