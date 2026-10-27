class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        swapPtr = length - 1
        while i < length:
            if nums[i] == val:
                nums[i], nums[swapPtr] = nums[swapPtr], nums[i]
                swapPtr -= 1
                length -= 1
            else:
                i += 1  
        
        return length