class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        directions = [
            (0, -1), (0, 1),
            (1, 0), (-1, 0)
        ]

        queue = collections.deque()
        freshCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        
        totalTime = 0
        while queue and freshCount > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                val = grid[row][col]

                # explore adjacent
                for dirY, dirX in directions:
                    finalR, finalC = row + dirY, dirX + col
                    if finalR in range(len(grid)) and finalC in range(len(grid[0])) and grid[finalR][finalC] == 1:
                        grid[finalR][finalC] = 2
                        freshCount -= 1
                        queue.append((finalR, finalC))
            totalTime += 1
        
        return totalTime if freshCount == 0 else -1
