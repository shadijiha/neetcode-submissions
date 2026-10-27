class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        
        row, col = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        cur_area = 0

        def dfs(r, c):
            nonlocal max_area
            nonlocal cur_area

            if (r, c) in visited:
                return
            if r not in range(row) or c not in range(col):
                return
            visited.add((r, c))

            if grid[r][c] != 1:
                return
            
            cur_area += 1
            max_area = max(max_area, cur_area)

            if r + 1 in range(row): dfs(r + 1, c)
            if r - 1 in range(row): dfs(r - 1, c)
            if c + 1 in range(col): dfs(r, c + 1)
            if c - 1 in range(col): dfs(r, c - 1)
            return

        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == 1:
                    cur_area = 0
                    dfs(r, c)
        
        return max_area