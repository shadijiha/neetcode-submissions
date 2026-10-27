class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}
        for i, n in enumerate(nums):
            map_[n] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map_ and i != map_[diff]:
                index = map_[diff]
                return [min(index, i), max(index, i)]
        
        return [-1, -1]