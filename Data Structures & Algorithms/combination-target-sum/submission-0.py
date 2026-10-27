class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(i, sol):
            s = sum(sol)
            if s == target:
                res.append(sol[:])
                return
            if i >= len(nums) or s > target:
                return
            
            sol.append(nums[i])
            backtrack(i, sol)
            sol.pop()
            backtrack(i + 1, sol)
            
        backtrack(0, [])
        return res