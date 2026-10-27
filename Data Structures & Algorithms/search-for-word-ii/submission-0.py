class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # revisit https://www.youtube.com/watch?v=asbcE9mZz_U&t=48s

        trie = TrieNode()
        for w in words:
            trie.insert(w)

        res, visited = set(), set()
        def backtrack(r, c, trieNode, currentSearchString):
            if r not in range(len(board)) or c not in range(len(board[r])) or \
                (r, c) in visited or board[r][c] not in trieNode.children:
                return

            visited.add((r, c))

            

            trieNode = trieNode.children[board[r][c]]
            currentSearchString = currentSearchString + board[r][c]
            
            if trieNode.isWord:
                res.add(currentSearchString)

            
            backtrack(r, c - 1, trieNode, currentSearchString)
            backtrack(r, c + 1, trieNode, currentSearchString)
            backtrack(r - 1, c, trieNode, currentSearchString)
            backtrack(r + 1, c, trieNode, currentSearchString)
            
            visited.remove((r, c))

        
        for r in range(len(board)):
            for c in range(len(board[r])):
                backtrack(r, c, trie, "")
        return list(res)