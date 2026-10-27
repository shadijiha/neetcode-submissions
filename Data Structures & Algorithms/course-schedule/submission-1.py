class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #
        # impossible = cycle
        # Topological sort

        # Adjancy list
        adj = {n: set() for n in range(numCourses) }
        for course, pre in prerequisites:
            adj[course].add(pre)

        # top sort
        visited = set()
        result = []

        def dfs(course, path):  # returns True if there's a cycle
            if course in path:
                return True
            if course in visited:
                return False
            path.add(course)
            for neighbour in adj[course]:
                if neighbour in visited: continue
                r = dfs(neighbour, path)
                if r:
                    return True

            path.remove(course)
            visited.add(course)
            result.append(course)
            return False
        
        for i in range(numCourses):
            if i not in visited:
                res = dfs(i, set())
                if res:
                    return False

        return len(result) == numCourses