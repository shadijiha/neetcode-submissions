class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #    [1, 2, 1]
        #                     []    
        #           1                   []
        #      [1, 2]       [1]       [2]      []
        #  [1,2,1] [1,2]  [1,1] [1]  [2,1] [2]  [1]   []
        nums.sort()
        res = []

        def backtrack(i, sol):
            if i >= len(nums):
                res.append(sol[:])
                return

            # include
            num = nums[i]
            sol.append(nums[i])     
            index = i + 1           
            backtrack(index, sol)

            # don't include
            sol.pop()

           
            while index < len(nums) and nums[index] == num:
                index += 1
            backtrack(index, sol)

        backtrack(0, [])
        return res