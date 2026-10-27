# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        nodes = deque([(root, 0)])

        while nodes:
            node, level = nodes.popleft()

            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))
            
            if level >= len(res):
                res.append([node.val])
            else:
                res[level].append(node.val)
    
        return res