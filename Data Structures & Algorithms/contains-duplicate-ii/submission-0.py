class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = {}

        for i, n in enumerate(nums):
            if n in nums_set and abs(i - nums_set[n]) <= k:
                return True
            nums_set[n] = i
        return False