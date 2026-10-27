from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        res = 0
        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return
            if i not in range(row) or j not in range(col):
                return
            
            if grid[i][j] == "1":
                visited.add((i, j))
                if i + 1 in range(row): dfs(i + 1, j) 
                if i - 1 in range(row): dfs(i - 1, j) 
                if j + 1 in range(col): dfs(i, j + 1) 
                if j - 1 in range(col): dfs(i, j - 1) 
            return
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
            
        return res