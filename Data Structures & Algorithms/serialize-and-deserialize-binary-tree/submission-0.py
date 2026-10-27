# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        str_array = []
        
        self.pre_order(root, lambda n: str_array.append(str(n)))

        return ",".join(str_array)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        str_array = data.split(",")
        return self.deserialize_recursively(str_array)

    def deserialize_recursively(self, data) -> TreeNode:
        if len(data) > 0:
            val = data.pop(0)

            if val == "null":
                return None

            node = TreeNode(val)
            left = self.deserialize_recursively(data)
            right = self.deserialize_recursively(data)
            node.left = left
            node.right = right
            return node
        return None

    def pre_order(self, root, func):
        if root is None:
            func("null")
            return
        
        func(root.val)
        self.pre_order(root.left, func)
        self.pre_order(root.right, func)
        return