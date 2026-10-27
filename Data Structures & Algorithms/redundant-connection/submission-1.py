class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parents = [i for i in range(0, N)]

        def find(x):
            if parents[x] == x:
                return x
            parents[x] = find(parents[x])
            return parents[x]
        
        redundant_edge = []

        def union(x1, x2):
            p1 = find(x1)
            p2 = find(x2)

            if p1 == p2:
                redundant_edge.append([x1 + 1, x2 + 1])
                return
            parents[p1] = p2
            return
        
        for x1, x2 in edges:
            union(x1 - 1, x2 - 1)

        return redundant_edge[-1] if len(redundant_edge) > 0 else []


