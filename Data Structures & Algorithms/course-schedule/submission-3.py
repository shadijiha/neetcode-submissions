class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        CYCLE, OK = 0, 1

        adj = defaultdict(set)
        for a, b in prerequisites:
            adj[b].add(a)
        
        # run top sort
        visited = set()

        def top_sort(node, path):
            if node in path:
                return CYCLE
            if node in visited:
                return OK
            
            visited.add(node)
            path.add(node)
            for neighbour in adj[node]:
                if top_sort(neighbour, path) == CYCLE:
                    return CYCLE
            path.remove(node)
            return OK
        
        for i in range(numCourses):
            if top_sort(i, set()) == CYCLE:
                return False
        
        return True