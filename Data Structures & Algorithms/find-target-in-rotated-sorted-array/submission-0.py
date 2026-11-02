class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotation_point = self.index_of_rotation_point(nums)

        arr1 = nums[:rotation_point]
        arr2 = nums[rotation_point:]

        result1 = self.binary_search(arr1, target)
        result2 = self.binary_search(arr2, target)

        if result2 != -1:
            result2 += rotation_point

        return result1 if result1 != -1 else result2

    
    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = ((r - l) // 2 ) + l

            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        return -1
        
    def index_of_rotation_point(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # important not <= otherwise infinit loop
        while l < r:
            m = ((r - l) // 2 ) + l

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m # not m - 1 because m itself might be the answer
        
        return l