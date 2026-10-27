# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = math.inf

        def dfs(root, index):
            nonlocal k
            nonlocal res

            if root is None:
                return index

            
            index = dfs(root.left, index)
            index += 1
            if index == k:
                res = root.val 
            index = dfs(root.right, index)
            return index

        dfs(root, 0)    

        return res