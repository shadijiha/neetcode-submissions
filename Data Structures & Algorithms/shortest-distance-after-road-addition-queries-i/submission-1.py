class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = defaultdict(set)

        for i in range(n - 1):
            adj[i].add(i + 1)
        
        res = []
        for query in queries:
            u, v = query
            adj[u].add(v)

            res.append(self.shortest(adj, n - 1))

        return res

    def shortest(self, graph, destination) -> int:
        START = 0
        # No need for Djiktra because the cost is alawys + 1
        q = deque([(0, START)])  # total cost, node
        visited = set()

        while q:
            cost, node = q.popleft()

            if node == destination:
                return cost

            if node in visited:
                continue
            visited.add(node)

            for neighbour in graph[node]:
                q.append(
                    (cost + 1, neighbour) 
                )
        return -1
