class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(set)
        email_to_name = {}

        for name, *emails in accounts:
            for e in emails:
                email_to_name[e] = name

                adj[e].add(emails[0])
                adj[emails[0]].add(e)
        
        result = []
        visited = set()
        def dfs(email, path):
            if email in visited:
                return
           
            visited.add(email)
            path.append(email)

            for neighbour in adj[email]:
                dfs(neighbour, path)

        for email in adj:
            if email in visited: continue

            path = list()
            dfs(email, path)

            result.append([
                email_to_name[email],
                *path
            ])
        
        return result
            

                