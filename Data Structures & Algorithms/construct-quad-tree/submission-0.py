"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False
                        break
            
            if all_same:
                return Node(grid[r][c], True)
            
            n = n // 2
            topleft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomleft = dfs(n, r + n, c)
            bottomright = dfs(n, r + n, c + n)

            return Node(
                grid[r][c], False, topleft,
                topRight, bottomleft, bottomright
            )
        return dfs(len(grid), 0, 0)





