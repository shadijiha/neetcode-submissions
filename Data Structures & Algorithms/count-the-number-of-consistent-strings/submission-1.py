class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(list(allowed))

        total = len(words)
        for w in words:
            for l in w:
                if l not in allowed:
                    total -= 1
                    break
        return total
                