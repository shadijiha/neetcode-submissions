class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        positive_diag = set() # (r - c)
        negative_diag = set() # (r + c)

        res = 0
        board = [ (["."] * n) for _ in range(n) ]

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if c in cols or (r + c) in negative_diag or (r - c) in positive_diag:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                negative_diag.add(r + c)
                positive_diag.add(r - c)
                
                backtrack(r + 1)

                cols.remove(c)
                negative_diag.remove(r + c)
                positive_diag.remove(r - c)
                board[r][c] = "."


        #for r in range(n):
        backtrack(0)
        
        return res