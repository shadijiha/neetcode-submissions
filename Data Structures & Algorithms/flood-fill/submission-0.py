class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return [[]]
        
        def dfs(r, c, colorToReplace):
            if r not in range(len(image)) or c not in range(len(image[0])):
                return
            
            pixel = image[r][c]
            if pixel != colorToReplace:
                return

            image[r][c] = color

            dfs(r, c - 1, colorToReplace)
            dfs(r, c + 1, colorToReplace)
            dfs(r - 1, c, colorToReplace)
            dfs(r + 1, c, colorToReplace)

        colorToReplace = image[sr][sc]
        if colorToReplace == color:
            return image
        dfs(sr, sc, colorToReplace)
        return image