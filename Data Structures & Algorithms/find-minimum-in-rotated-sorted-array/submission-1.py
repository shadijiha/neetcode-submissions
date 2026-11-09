class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        #  l   m     r
        #        l m r
        #        l r  
        #        m r
        #          lr
        return nums[self._find_rotation_point(nums)]         
    
    def _find_rotation_point(self, nums) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = ((r - l) // 2) + l

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l
