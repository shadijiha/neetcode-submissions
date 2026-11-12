class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # [1,2,3,1]
        #. ^
        #
        #dp.  1     2   3   1 
        #. A.       2   3   1
        #. B   

        memo = {}
        def backtrack(l, r) -> int:
            if r - l + 1 == 0:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            left = piles[l] - backtrack(l + 1, r)
            right = piles[r] - backtrack(l, r - 1)

            memo[(l, r)] = max(left, right)
            return memo[(l, r)]
        
        res = backtrack(0, len(piles) - 1)
        return res > 0
