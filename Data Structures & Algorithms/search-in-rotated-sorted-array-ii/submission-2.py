class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        # [3,4,5,6,1,2]
        #        ^   ^
        l, r = 0, len(arr) - 1

        while l <= r:
            m = ((r - l) // 2) + l

            if arr[m] == target:    return True

            if arr[m] > target:
                if arr[l] <= target <= arr[m]:
                    r = m - 1
                else:
                    l += 1
            elif arr[m] < target:
                if arr[m] <= target <= arr[r]:
                    l = m + 1
                else:
                    r -= 1
            else:
                l += 1
        return False

    # def _get_pivot_point(self, nums):
    #     l, r = 0, len(nums) - 1

    #     while l < r:
    #         m = ((r - l) // 2) + l

    #         if nums[m] > nums[r]:
    #             l = m + 1
    #         elif nums[m] < nums[r]:
    #             r = m
    #         else:
    #             r -= 1
    #     return l
