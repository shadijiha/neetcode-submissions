class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0]) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save topleft 
                topLeft = matrix[top][l + i]

                # do the rotation in reverse order
                matrix[top][l + i] = matrix[bottom - i][l]

                # move the bottom right 
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move the top right
                matrix[bottom][r - i] = matrix[top + i][r]

                # put back the saved top left value
                matrix[top + i][r] = topLeft
            
            l += 1
            r -= 1