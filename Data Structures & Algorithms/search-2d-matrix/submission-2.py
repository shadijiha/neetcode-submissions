class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find which row to search
        rowIndex = -1

        for i, row in enumerate(matrix):
            if target <= row[len(row) - 1] and target >= row[0]:
                rowIndex = i
        print(rowIndex)
        if rowIndex == -1:
            return False
        
        # binary search on row
        row = matrix[rowIndex]
        l, r = 0, len(row) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target < row[m]:
                r = m - 1
            elif target > row[m]:
                l = m + 1
            else: 
                return True
        return False