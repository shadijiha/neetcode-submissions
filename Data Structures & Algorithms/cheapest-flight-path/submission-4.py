class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(set)

        for fromm, to, price in flights:
            adj[fromm].add( (to, price) )
        
        q = [(0, src, 0)] # priority q (airport, totalCost, totalStops)
        best = {}

        while q:
            cost, airport, stops = heapq.heappop(q)

            if airport == dst:
                return cost
            
            if stops >= k + 1:
                continue

            if cost > best.get((airport, stops), math.inf):
                continue
            best[(airport, stops)] = min(cost, best.get((airport, stops), math.inf))

            for neighbour, neighbourCost in adj[airport]:
                heapq.heappush(q, (cost + neighbourCost, neighbour, stops + 1))
        
        return -1
            