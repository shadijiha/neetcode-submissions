class TrieNode:
    def __init__(self):
        #self.neighbours = [None] * 26
        self.neighbours = {}
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.maxWordSize = 0
        

    def addWord(self, word: str) -> None:
        self.maxWordSize = max(self.maxWordSize, len(word))
        cur = self.root

        for c in word:
            if c not in cur.neighbours:
                cur.neighbours[c] = TrieNode()
            cur = cur.neighbours[c]
        cur.isLeaf = True
        
    def search(self, word: str, current=None) -> bool:
        if len(word) > self.maxWordSize:
            return False

        def dfs(start, root):
            cur = root
            for i in range(start, len(word)):
                c = word[i]
                if c == '.':
                    for n in cur.neighbours.values():
                        if dfs(i + 1, n): return True
                    return False
                else:
                    if c not in cur.neighbours:
                        return False
                    cur = cur.neighbours[c]

            return cur.isLeaf
        
        return dfs(0, self.root)
        
