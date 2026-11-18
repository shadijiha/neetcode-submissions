class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(set)
        outgoing = defaultdict(int)

        for a, b in trust:
            adj[b].add(a)
            outgoing[a] += 1

        print(adj)
        for key in adj:
            if len(adj[key]) == n - 1 and outgoing[key] == 0:
                return key
        
        return -1