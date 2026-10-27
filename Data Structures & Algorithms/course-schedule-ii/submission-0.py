class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #
        # impossible = cycle
        # Topological sort
        adj = {n: set() for n in range(numCourses)}

        for course, pre in prerequisites:
            adj[pre].add(course)
        
        # Top sort algorithm
        result = []

        visited = set()

        def dfs(course, path) -> bool:
            if course in path:
                return True
            if course in visited:
                return False
            
            path.add(course)

            for neighbour in adj[course]:
                if neighbour in visited: continue
                if dfs(neighbour, path): return True
            
            result.append(course)
            path.remove(course)
            visited.add(course)
            return False

        for course in range(numCourses):
            if dfs(course, set()): return []

        result.reverse()
        return result
