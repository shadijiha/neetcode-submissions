# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, height) -> int:
            nonlocal res
            if node is None:
                return height
            
            heightL = dfs(node.left, height)
            heightR = dfs(node.right, height)

            res = max(res, heightL + heightR)

            return max(heightL, heightR) + 1

        dfs(root, 0)
        return res