"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}
        

        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]
            
            clonedNode = Node(node.val)
            cloneMap[node] = clonedNode
            for n in  node.neighbors:
                clonedNode.neighbors.append(dfs(n))
            
            return clonedNode
        
        return dfs(node) if node else None