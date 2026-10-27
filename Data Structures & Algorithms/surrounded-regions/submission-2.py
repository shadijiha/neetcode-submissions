class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(r, c):
            if r not in range(len(board)) or c not in range(len(board[r])):
                return

            if board[r][c] != "O":
                return False
            
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            board[r][c] = "T"
            for i, j in directions:
                finalR, finalC = r + i, c + j
                dfs(finalR, finalC)
      
            
        for c in range(len(board[0])):
            dfs(0, c)
            dfs(len(board) - 1, c)
        
        for r in range(len(board)):
            dfs(r, 0)
            dfs(r, len(board[0]) - 1)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
