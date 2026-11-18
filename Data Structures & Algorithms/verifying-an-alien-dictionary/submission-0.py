class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        adj = defaultdict(set)
        order = {c: i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            str1 = words[i - 1]
            str2 = words[i]

            if len(str1) > len(str2) and str1.startswith(str2):
                return False
            
            for i in range(min(len(str1), len(str2))):
                if str1[i] == str2[i]:
                    continue
                adj[str1[i]].add(str2[i])
                break

        for key in adj:
            for c in adj[key]:
                if order[c] < order[key]:
                    return False

        return True
            
            
