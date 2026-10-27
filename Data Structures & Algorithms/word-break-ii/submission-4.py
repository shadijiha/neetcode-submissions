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
        # WITH CACHING (scroll for no caching => simpler)
        wordDict = set(wordDict)
        trie = TrieNode()
        for w in wordDict:
            trie.insert(w)

        memo = {}
        def dfs(i):
            if i >= len(s):
                return [""]
            if i in memo:
                return memo[i]

            res = []
            node = trie
            for j in range(i, len(s)):
                char = s[j]

                if char not in node.children:
                    break

                node = node.children[char]
                if node.isWord:
                    word = s[i:j+1]
                    strings = dfs(j + 1)
                    if not strings:
                        continue
                    
                    for substring in strings:
                        sentence = word
                        if substring:
                            sentence += " " + substring
                        res.append(sentence)
            memo[i] = res
            return res       

        return dfs(0)


        # WITHOUT CACHING
        # wordDict = set(wordDict)
        # trie = TrieNode()
        # for w in wordDict:
        #     trie.insert(w)

        # res = []

        # def dfs(i, sol):
        #     if i >= len(s):
        #         res.append(" ".join(sol))
        #         return
            
        #     node = trie
        #     for j in range(i, len(s)):
        #         char = s[j]

        #         if char not in node.children:
        #             break

        #         node = node.children[char]
        #         if node.isWord:
        #             substr = s[i:j+1]
        #             sol.append(substr)
        #             dfs(j + 1, sol)
        #             sol.pop()

        # dfs(0, [])
        # return res


