class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #                 []
        #       [1]       [2]         [3]
        #      2   3    1  3   [] 1 2
        #      3   2

        res = []

        def backtrack(index, sol):
            if index >= len(nums):
                res.append(sol[:])
                return
            
            # add
            sol.append(nums[index])
            backtrack(index + 1, sol)

            # not add
            sol.pop()
            backtrack(index + 1, sol)

        backtrack(0, [])
        return res