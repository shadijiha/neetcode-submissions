class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            directions = [
                [0, 1], [0, -1], [1, 0], [-1, 0]
            ]

            longest = 1

            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if not (0 <= x < ROWS and 0 <= y < COLS):
                    continue

                if matrix[x][y] > matrix[i][j]:
                    longest = max(longest, 1 + dfs(x, y))

            memo[(i, j)] = longest
            return longest

        max_path = 0

        for r in range(ROWS):
            for c in range(COLS):
                max_path = max(max_path, dfs(r, c))

        return max_path