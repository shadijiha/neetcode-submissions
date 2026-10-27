class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # [9,2,6], 8
        #                      []
        #       9                          []     
        #                          2               []
        #                      6       []       6         []
        #                   8                2                  []
        candidates.sort()
        res = []

        def backtrack(i, sol, total, lastDigit):
            if total == target:
                res.append(sol[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            cand = candidates[i]
            lastDigit = cand
            sol.append(cand)
            backtrack(i + 1, sol, total + cand, lastDigit)
            sol.pop()

            while i < len(candidates) and candidates[i] == lastDigit:
                i += 1
            backtrack(i, sol, total, lastDigit)


        backtrack(0, [], 0, None)
        return res