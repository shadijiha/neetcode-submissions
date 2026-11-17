class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        sol = []

        def backtrack(used):
            if len(sol) == len(nums):
                result.add(tuple(sol))
                return
            
            for i in range(len(nums)):
                if i in used: continue
                used.add(i)
                sol.append(nums[i])
                backtrack(used)
                sol.pop()
                used.remove(i)

        backtrack(set())

        return [list(n) for n in result]