class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        positive_dia = set() # r - c
        negative_dia = set() # r + c

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                board_as_str = ["".join(row) for row in board]
                res.append(board_as_str)
                return
            
            for c in range(n):
                if c in col:
                    continue
                if r + c in negative_dia:
                    continue
                if r - c in positive_dia:
                    continue

                col.add(c)
                negative_dia.add(r + c)
                positive_dia.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                board[r][c] = "."
                col.remove(c)
                positive_dia.remove(r - c)
                negative_dia.remove(r + c)
                
        
        backtrack(0)
        return res