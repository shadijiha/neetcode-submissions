from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word)
        
        shortestPath = 1
        visited = set([beginWord])
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return shortestPath
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbour in adj[pattern]:
                        if neighbour in visited: continue
                        visited.add(word)
                        q.append(neighbour)

            shortestPath += 1

        

        return 0
        
        # DFS Solution
        # if endWord not in wordList:
        #     return 0
        
        # adj = collections.defaultdict(set)

        # for word1 in [beginWord, *wordList]:
        #     for word2 in wordList:
        #         if word1 == word2: continue
        #         assert len(word1) == len(word2)
        #         charDiff = 0
        #         for i in range(len(word1)):
        #             if charDiff > 1: break
        #             if word1[i] != word2[i]:
        #                 charDiff += 1
        #         if charDiff == 1:
        #             adj[word1].add(word2)
        
        # minPath = math.inf
        # visited = set()
        
        # def dfs(node, path) -> bool:
        #     nonlocal minPath
        #     if node in path:
        #         return
            
        #     if node == endWord:
        #         minPath = min(minPath, len(path) + 1)
        #         return

        #     path.add(node)
        #     for n in adj[node]:
        #         dfs(n, path)
        #     path.remove(node) 

        # dfs(beginWord, set())

        # return minPath if minPath != math.inf else 0

