class Solution:
    def knightDialer(self, n: int) -> int:
        import sys
        sys.setrecursionlimit(10000)

        pad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [None, 0, None]
        ]

        memo = {}
        def backtrack(i, j, n):
            if n == 0:
                memo[(i, j, n)] = 1
                return memo[(i, j, n)]

            if (i, j, n) in memo:
                return memo[(i, j, n)]

            directions = [
                (1, 2), (-1, 2), (1, -2), (-1, -2),
                (2, 1), (-2, 1), (2, -1), (-2, -1),
            ]

            total = 0
            for dy, dx in directions:
                nexti, nextj = dy + i, dx + j
                if nexti not in range(len(pad)) or nextj not in range(len(pad[0])) or pad[nexti][nextj] == None:
                    continue
                total += backtrack(nexti, nextj, n - 1)
            
            memo[(i, j, n)] = total
            return total

        total = 0
        for r in range(len(pad)):
            for c in range(len(pad[r])):
                if pad[r][c] == None: continue
                total += backtrack(r, c, n - 1)

        return total % 1000000007
