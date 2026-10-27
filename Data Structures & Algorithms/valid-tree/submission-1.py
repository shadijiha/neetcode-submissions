class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]

        def find(x):
            if parents[x] == x:
                return x
            return find(parents[x])
        
        def union(x1, x2):
            p1 = find(x1)
            p2 = find(x2)

            if p1 == p2:
                return None
            
            parents[p1] = p2
            return 1

        total = n
        for x1, x2 in edges:
            if union(x1, x2):
                total -= 1
            else:
                return False
        
        print(total)
        return total == 1