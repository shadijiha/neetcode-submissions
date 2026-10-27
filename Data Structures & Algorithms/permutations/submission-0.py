class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #
        #                   *
        #      1            2           3
        #   2      3      1    3       1   2
        #   3      2      3    1       2   1

        # 1, 2
        res = []

        def backtrack(sol, used):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for num in nums:  
                if num in used:
                    continue

                sol.append(num)  # sol: [1]
                used.add(num)
                backtrack(sol, used)
                sol.pop()
                used.remove(num)

        backtrack([], set())
        return res