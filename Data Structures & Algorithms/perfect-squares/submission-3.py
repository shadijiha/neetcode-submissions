class Solution:
    def numSquares(self, n: int) -> int:
        # []
        #
        #
        import sys
        sys.setrecursionlimit(100000)
        memo = {}
        def backtrack(cumulative):
            if cumulative == n:
                return 0
            if cumulative > n:
                return math.inf
            
            if cumulative in memo:
                return memo[cumulative]

            minn = math.inf
            for i in range(1, int((n - cumulative)**0.5) + 1):
                total_used = 1 + backtrack(cumulative + i*i)
                minn = min(minn, total_used)

            memo[cumulative] = minn
            return minn
        
        return backtrack(0)