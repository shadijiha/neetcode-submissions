# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        q = deque([root])
        level = 0
        while q:
            q_len = len(q)
            values = []
            for _ in range(q_len):
                node = q.popleft()
                values.append(node.val)
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            for v in values:
                if v % 2 == level % 2:
                    return False
            
            
            odd = level % 2 != 0
            if values != sorted(set(values), reverse=odd):
                return False
            level += 1
        
        return True