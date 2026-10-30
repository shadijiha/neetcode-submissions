class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        q = [(0, 
            (points[0][0], points[0][1])
        )] # (cost, point)

        total_cost = 0
        while q:
            cost, (x, y) = heapq.heappop(q)

            if (x, y) in visited:
                continue
            visited.add((x, y))
            total_cost += cost
            
            if len(visited) == len(points):
                return total_cost
            
            

            for x2, y2 in points:
                if x2 == x and y2 == y: continue
                distance = abs(x - x2) + abs(y - y2)
                heapq.heappush(q, (distance, (x2, y2)))

        return -1

