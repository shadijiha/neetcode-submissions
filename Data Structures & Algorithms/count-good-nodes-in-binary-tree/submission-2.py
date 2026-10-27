# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
    
        def dfs(root, maxValue):
            nonlocal res
            if root is None:
                return
            
            if maxValue is None or root.val >= maxValue:
                res += 1
            
            if maxValue is None:
                maxValue = root.val
            else:
                maxValue = max(maxValue, root.val)
           
            left = dfs(root.left, maxValue)
            right = dfs(root.right, maxValue)

        dfs(root, None)
        return res
        
            