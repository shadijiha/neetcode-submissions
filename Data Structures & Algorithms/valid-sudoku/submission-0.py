class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        cells = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                e = board[r][c]
                if e == ".":
                     continue
                
                if e in row[r] or e in col[c] or e in cells[(r // 3,c // 3)]:
                    return False
                
                row[r].add(e)
                col[c].add(e)
                cells[(r // 3, c // 3)].add(e)
        return True
            


