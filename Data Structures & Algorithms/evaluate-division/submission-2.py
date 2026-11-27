class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # C / D
        # A / B = C
        # C / D = E

        adj = defaultdict(set)

        for i in range(len(equations)):
            a, b = equations[i]
            result = values[i]

            adj[a].add((b, result))
            adj[b].add((a, 1.0 / result))
            adj[a].add((a, 1.0))
        
        results = []
        for query in queries:
            a, b = query
            # Convert to regular dict so BFS does not insert missing nodes 
            # and loop forever
            results.append(self._bfs(dict(adj), a, b))
        
        return results
        
    
    def _bfs(self, graph: Dict[str, Set[Tuple[str, float]]], start_node: str, end_node: str) -> float:
        if start_node not in graph or end_node not in graph:
            return -1.0
            
        q = deque([(start_node, 1.0)])
        visited = set()

        while q:
            node, cumulitive  = q.popleft()

            if node == end_node:
                return cumulitive
            
            if node in visited:
                continue
            visited.add(node)
            
            for neighbour in graph[node]:
                next_node, next_division = neighbour
                q.append(
                    (next_node, cumulitive * next_division)
                )
        
        return -1.0