class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #
        #    [1,2,0],
        #    [5,4,2],
        #    [1,1,3]
        #
        #dp= [
        #     []
        #     [4  4  5]
        #     [5, 4, 3] 
        #   ]
        #
        N, M = len(grid), len(grid[0])
        dp = [([0] * M) for _ in range(N)]
        dp[-1][-1] = grid[-1][-1]

        for i in reversed(range(N)):
            for j in reversed(range(M)):
                if i == N - 1 and j == M - 1: continue
                
                right = dp[i + 1][j] if i + 1 < N else math.inf
                bottom = dp[i][j + 1] if j + 1 < M else math.inf 
                curr = grid[i][j]
                dp[i][j] = curr + min(right, bottom)

        return dp[0][0]