class Solution:
    def rob(self, nums: List[int]) -> int:
        # [3,4,3,2]
        #                        *           
        #            3           4          3          
        #       3       2        2          3 (circle)
        #   
        #       6       5        6          6           
        #
        if len(nums) == 1:
            return nums[0]
        HOUSES = len(nums)

        # include the first house = exclude last
        dp1 = [0 for _ in range(HOUSES + 1)]         # [0, 0, 0, 3]
        dp1[HOUSES] = 0
        dp1[HOUSES - 1] = 0

        for i in reversed(range(HOUSES - 1)):
            dp1[i] = max(dp1[i + 1], nums[i] + dp1[i + 2])

        # include last = exclude first
        dp2 = [0 for _ in range(HOUSES + 1)]
        dp2[HOUSES] = 0
        dp2[HOUSES - 1] = nums[-1]

        for i in reversed(range(HOUSES - 1)):
            if i == 0:
                continue
            dp2[i] = max(dp2[i + 1], nums[i] + dp2[i + 2])
            

        return max(dp1[0], dp2[1])
