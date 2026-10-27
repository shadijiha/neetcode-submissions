# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inOrder(root)[k - 1]
    

    def inOrder(self, root) -> List[int]:
        if root is None:
            return []
        
        left = self.inOrder(root.left)
        right = self.inOrder(root.right)

        return [*left, root.val, *right]
        