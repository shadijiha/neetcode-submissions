class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) # not -1
        top, bottom = 0, len(matrix)

        result = []

        while left < right and top < bottom:
            # left to right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # right column
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            
            # for columnm and row matrices
            if not (left < right and top < bottom):
                break

            # bottom row
            for i in reversed(range(left, right)):
                result.append(matrix[bottom - 1][i]) 
            bottom -= 1

            # left col
            for i in reversed(range(top, bottom)):
                result.append(matrix[i][left])
            left += 1

        return result
