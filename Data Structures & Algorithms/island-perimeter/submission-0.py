class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [
            (0, 1), (1, 0), (-1, 0), (0, -1)
        ]

        visited = set()
        total = 0

        def dfs(i, j):
            nonlocal total

            if i not in range(ROWS) or j not in range(COLS):
                total += 1
                return

            if grid[i][j] == 0:
                total += 1
                return

            if (i, j) in visited:
                return
            
            visited.add((i, j))
   
            dfs(i + 1, j)
            dfs(i - 1, j)  
            dfs(i, j + 1)
            dfs(i, j - 1)     

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return total
        return 0