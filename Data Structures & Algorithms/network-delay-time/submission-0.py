class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return -1
        
        # Adjancy list
        edges = collections.defaultdict(list)       
        #   { 2: [ (3, 1) ]
        #     1: [ (1, 1), (1, 4) ] 
        #   }
        for u, v, t in times:
            edges[u].append((v, t))

        visited = set()
        queue = [(0, k)]
        heapq.heapify(queue)

        maxDelay = 0

        while queue:
            weight, nodeVal = heapq.heappop(queue)
            if nodeVal in visited:
                continue
            
            visited.add(nodeVal)
            maxDelay = max(maxDelay, weight)

            for dst, weightDst in edges[nodeVal]:
                if dst in visited:
                    continue
                totalWeight = weight + weightDst
                heapq.heappush(queue, (totalWeight, dst))

        return maxDelay if len(visited) == n else -1