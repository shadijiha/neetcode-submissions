# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(node) -> (int, int):
            if not node:
                return 0, 0

            # If we choose current node
            with_node_left, without_node_left = helper(node.left)
            with_node_right, without_node_right = helper(node.right)

            return (
                node.val + without_node_left + without_node_right,
                max(with_node_left + with_node_right, without_node_left + without_node_right, with_node_left + without_node_right, without_node_left + with_node_right)
            )
        
        return max(*helper(root))