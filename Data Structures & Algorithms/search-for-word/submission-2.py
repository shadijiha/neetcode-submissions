class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        def dfs(r, c, currentCharSearch) -> bool:
            if currentCharSearch == len(word):
                return True
            if r not in range(len(board)) or c not in range(len(board[0])) or ((r, c) in visited) or word[currentCharSearch] != board[r][c]:
                return False
            
            visited.add((r, c))
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rDir, cDir = r + x, c + y
                
                res = dfs(rDir, cDir, currentCharSearch + 1)
                
                if res:
                    return True
            visited.remove((r, c))
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                res = dfs(row, col, 0)
                if res:
                    return True  
        return False
