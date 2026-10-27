from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            r, c = q.popleft()

            for dx, dy in directions:
                newR, newC = r + dx, c + dy

                if newR in range(ROWS) and newC in range(COLS) \
                    and grid[newR][newC] == 2147483647:
                    grid[newR][newC] = grid[r][c] + 1
                    q.append((newR, newC))


