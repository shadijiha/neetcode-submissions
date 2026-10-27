class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]


        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return x
        
        def union(x1, x2):
            p1 = parents[find(x1)]
            p2 = parents[find(x2)]

            if p1 == p2:
                return 0 # already connected
            else:
                parents[p1] = p2
                return 1

        res = n
        for e in edges:
            x1, x2 = e
            res -= union(x1, x2)

        return res 