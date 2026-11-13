class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        #
        # backtrack result is the max score difference
        #
        N = len(piles)
        
        memo = {}
        def backtrack(l, M):
            if l >= N:
                memo[(l, M)] = 0
                return memo[(l, M)]
            
            if (l, M) in memo:
                return memo[(l, M)]
            
            max_score_diff = -math.inf
            for X in range(1, 2 * M + 1):
                if X + l > N: break

                subarray_sum = sum(piles[l:l+X])
                res = subarray_sum - backtrack(l + X, max(X, M))
                max_score_diff = max(max_score_diff, res)

            memo[(l, M)] = max_score_diff
            return max_score_diff

        return (backtrack(0, 1) + sum(piles)) // 2