CYCLE_DETECTED = False
OK = True

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        # build adj
        for i in range(0, len(words) - 1):
            s1 = words[i]
            s2 = words[i + 1]
            
            if len(s1) > len(s2) and s1.startswith(s2):
                return ""

            for j in range(min(len(s1), len(s2))):
                if s1[j] == s2[j]: continue

                c1 = s1[j]
                c2 = s2[j]
                if c1 not in adj:
                    adj[c1] = set([c2])
                else:
                    adj[c1].add(c2)
                break

        # top sort
        visited = set()
        result = []
        def dfs(char, path):
            if char in path:
                return CYCLE_DETECTED

            if char in visited:
                return OK

            path.add(char)

            for neighbour in (adj[char] if char in adj else []):
                if dfs(neighbour, path) == CYCLE_DETECTED:
                    return CYCLE_DETECTED

            result.append(char)
            path.remove(char)
            visited.add(char)
            return OK

        for c in adj:
            if dfs(c, set()) == CYCLE_DETECTED:
                return ""

        return "".join(result[::-1])