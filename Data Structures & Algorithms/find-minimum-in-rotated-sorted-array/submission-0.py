class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotation_index = self.index_of_rotation_point(nums)
        return nums[rotation_index]
    

    def index_of_rotation_point(self, nums) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = ((r - l) // 2) + l

            #[3,4,5,6,1,2]
            # ^   ^     ^
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return l
        
        