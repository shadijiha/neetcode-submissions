class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)

        for a, b in prerequisites:
            adj[a].add(b)
        

        memo = {}
        def top_sort(course, destination, path) -> bool:
            if (course, destination) in memo:
                return memo[(course, destination)]

            if course in path:
                memo[(course, destination)] = False
                return False
            
            if course == destination:
                memo[(course, destination)] = True
                return True
                
            path.add(course)
            for neighbour in adj[course]:
                if top_sort(neighbour, destination, path):
                    return True
            path.remove(course)
            memo[(course, destination)] = False
            return False
        
        result = [False] * len(queries)
        for i, q in enumerate(queries):
            u, v = q
            if top_sort(u, v, set()):
                result[i] = True
            
        return result