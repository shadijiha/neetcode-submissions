class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        rows_to_zero = set()
        cols_to_zero = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows_to_zero.add(r)
                    cols_to_zero.add(c)
        
        for r in rows_to_zero:
            for c in range(COLS):
                matrix[r][c] = 0
        
        for r in range(ROWS):
            for c in cols_to_zero:
                matrix[r][c] = 0
        
        