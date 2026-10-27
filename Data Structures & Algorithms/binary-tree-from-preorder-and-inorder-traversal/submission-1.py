# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # optimized
        indices = { value:i for i, value in enumerate(inorder) }

        def recursiveBuild(inOrderStart, inOrderEnd):
            if inOrderStart > inOrderEnd:
                return None
            
            root = TreeNode(preorder.pop(0))
            index = indices[root.val]

            root.left = recursiveBuild(inOrderStart, index - 1)
            root.right = recursiveBuild(index + 1, inOrderEnd)

            return root
        
        return recursiveBuild(0, len(inorder) - 1)

        # non optimized
        #
        # if not inorder:
        #     return None

        # root = TreeNode(preorder.pop(0))
        # index = inorder.index(root.val)

        # root.left = self.buildTree(preorder, inorder[:index])
        # root.right = self.buildTree(preorder, inorder[index+1:])

        # return root