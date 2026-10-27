class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return -1

        #adjancy list
        edges = collections.defaultdict(list)
        # {
        #   (0,0):  [(dist, (2,2))]
        #}
        for i, p in enumerate(points):
            x, y = p
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                
                x2, y2 = p2
                dist = abs(x - x2) + abs(y - y2)
                edges[(x, y)].append( (dist , (x2, y2)) )

        minDistance = 0
        visited = set()
        firstX, firstY = points[0]
        q = [(0, (firstX, firstY) )]
        heapq.heapify(q)

        while q:
            distance, point = heapq.heappop(q)
            if point in visited:
                continue

            visited.add(point)
            minDistance += distance
            
            for dist, p in edges[point]:
                if p in visited:
                    continue
                px, py = p
                heapq.heappush(q, (dist, (px, py)))

        return minDistance

