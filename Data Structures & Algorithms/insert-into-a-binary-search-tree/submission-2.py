# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int, prevNode = None) -> Optional[TreeNode]:
        if root is None and prevNode is None:
            return TreeNode(val)
        
        if root is None:
            if val > prevNode.val:
                prevNode.right = TreeNode(val)
            else:
                prevNode.left = TreeNode(val)
            return root
        
        if val < root.val:
            self.insertIntoBST(root.left, val, root)
        else:
            self.insertIntoBST(root.right, val, root)

        return root