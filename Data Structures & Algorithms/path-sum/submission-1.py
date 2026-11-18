# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, total):
            if not root:
                return False
            if not root.left and not root.right:
                return total + root.val == targetSum
            
            left = helper(root.left, total + root.val)
            right = helper(root.right, total + root.val)

            return left or right

        return helper(root, 0)