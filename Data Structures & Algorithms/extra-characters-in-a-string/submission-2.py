class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    
    def has_word(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #
        #                       *
        #               n              -
        #          e        -              e
        #       e               -
        #   t
        #
        dictionary = set(dictionary)
        trie = Trie()
        for w in dictionary:
            trie.insert(w)

        memo = {}
        def backtrack(i) -> int:
            if i >= len(s):
                return 0
            
            if i in memo:
                return memo[i]
            
            # Choice 1: Skip the char
            res = 1 + backtrack(i + 1)

            # Choice 2: Find words starting at i
            node = trie.root
            for j in range(i, len(s)):
                #temp = s[i:j+1]
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]

                #if temp in dictionary:
                if node.isWord:
                    res = min(res, backtrack(j + 1))

            memo[i] = res
            return memo[i]
    
        return backtrack(0)
            
