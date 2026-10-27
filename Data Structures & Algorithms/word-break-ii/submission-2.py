class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def insert(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        trie = TrieNode()
        for w in wordDict:
            trie.insert(w)

        res = []

        def dfs(i, sol):
            if i >= len(s):
                res.append(" ".join(sol))
                return
            
            node = trie
            for j in range(i, len(s)):
                char = s[j]

                if char not in node.children:
                    break

                node = node.children[char]
                if node.isWord:
                    substr = s[i:j+1]
                    sol.append(substr)
                    dfs(j + 1, sol)
                    sol.pop()

        dfs(0, [])
        return res


