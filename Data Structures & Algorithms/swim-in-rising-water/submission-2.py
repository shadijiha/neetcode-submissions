class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        ROWS, COLS = len(grid), len(grid[0])
        adj = collections.defaultdict(list)    # (r,c): (newR, newC)

        # This adj is weird because it isn't really necessary,
        # We don't need to establish weights in this problem
        # because we need to just keep track of the maxHeight so far in Dijktra while loop
        # THis is not really necessary, in theory
        for r in range(ROWS):
            for c in range(COLS):
                for dx, dy in directions:
                    newR, newC = r + dy, c + dx
                    if newR in range(ROWS) and newC in range(COLS):
                        adj[(r, c)].append((newR, newC)) 
        
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
                nR, nC = neighbour
                newCost = max(cost, grid[nR][nC])
                heapq.heappush(q,
                    ( newCost, (nR, nC) )
                )
        return minRes
                