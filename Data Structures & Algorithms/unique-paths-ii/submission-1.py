class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #
        #    [0,0,1],
        #    [0,0,0],
        #    [0,1,0]
        #
        #    let dp[i][j] be unique path from i,j to n-1, m-1   
        #    
        # dp[n-1][m-1] = 1
        #
        #dp= [0,3,1],
        #    [0,1,1],
        #    [0,0,1]
        #
        #
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        dp = [([0] * M) for _ in range(N)]
        dp[-1][-1] = 1 if obstacleGrid[-1][-1] == 0 else 0

        for i in reversed(range(N)):
            for j in reversed(range(M)):
                if i == N - 1 and j == M - 1: continue

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    right = dp[i][j + 1] if j + 1 < M else 0
                    bottom = dp[i + 1][j] if i + 1 < N else 0
                    dp[i][j] = right + bottom

        print(dp)
        return dp[0][0]