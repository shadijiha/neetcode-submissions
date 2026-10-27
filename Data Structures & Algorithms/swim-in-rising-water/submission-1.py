class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        ROWS, COLS = len(grid), len(grid[0])
        adj = collections.defaultdict(list)    # (r,c): (cost, (newR, newC)) 

        for r in range(ROWS):
            for c in range(COLS):
                for dx, dy in directions:
                    newR, newC = r + dy, c + dx
                    if newR in range(ROWS) and newC in range(COLS):
                        cost = max(0, grid[newR][newC] - grid[r][c])
                        adj[(r, c)].append( (cost, (newR, newC)) ) 
        
        visited = set()
        q = [(grid[0][0], (0, 0))]  # (cost, (r, c))
        minRes = math.inf

        while q:
            cost, (r, c) = heapq.heappop(q)
            
            if (r, c) in visited:
                continue
            visited.add((r, c))

            
            # if destination
            if r == ROWS - 1 and c == COLS - 1:
                minRes = min(minRes, cost)
        
            # visite each neighbour
            for neighbour in adj[(r, c)]:
                weight, (nR, nC) = neighbour
                newCost = max(cost, grid[nR][nC])
                heapq.heappush(q,
                    ( newCost, (nR, nC) )
                )
        return minRes
                