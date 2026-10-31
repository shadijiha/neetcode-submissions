class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 0/1 Knapsack, bottom up is too hard https://youtu.be/dwMOrl85Xes?si=C5pbdHh28ax8IFGH&t=1104
        #
        #                       *
        #                2
        #           2
        #      -2
        #      

        memo = {}
        def backtrack(i, backtrack_target):
            if i >= len(nums):
                if backtrack_target == 0:
                    return 1
                return 0
            
            if (i, backtrack_target) in memo:
                return memo[(i, backtrack_target)]
            
            num = nums[i]
            ways_positive = backtrack(i + 1, backtrack_target - num)
            ways_negative = backtrack(i + 1, backtrack_target + num)

            res = ways_positive + ways_negative
            memo[(i, backtrack_target)] = res

            return res
        
        return backtrack(0, target)