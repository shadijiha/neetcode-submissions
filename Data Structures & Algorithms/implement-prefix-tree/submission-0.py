class TrieNode:
    def __init__(self):
        self.neighbours: List[TrieNode] = [None] * 26
        self.isLeaf = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            n = curr.neighbours[index]
            if n is None:
                node = TrieNode()
                curr.neighbours[index] = node
            curr = curr.neighbours[index]

        curr.isLeaf = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if curr.neighbours[index] is None:
                return False
            curr = curr.neighbours[index]
        return curr.isLeaf
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            index = ord(c) - ord('a')
            if curr.neighbours[index] is None:
                return False
            curr = curr.neighbours[index]
        return True
        
        