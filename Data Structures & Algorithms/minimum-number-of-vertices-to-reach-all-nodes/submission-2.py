class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parents = [x for x in range(n)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
                return parents[x]
            return x 
        
        result = set([x for x in range(n)])
        def union(x1, x2):
            p1 = find(x1)
            p2 = find(x2)

            if p1 == p2:
                if x2 in result:
                    result.remove(x2)
                return
            else:
                parents[x1] = p1
                parents[x2] = p1

                if x2 in result:
                    result.remove(x2)
                return

        for fromm, to in edges:
            union(fromm, to)
        return list(result)