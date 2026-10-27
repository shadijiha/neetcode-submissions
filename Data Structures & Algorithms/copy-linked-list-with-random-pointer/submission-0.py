"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        dummy = Node(0, None)
        prevCopy = None
        copyIt = dummy
        originalIt = head


        while originalIt:
            newNode = Node(originalIt.val, None, originalIt.random)
            copyIt.next = newNode

            if prevCopy:
                prevCopy.next = newNode

            old_to_new[originalIt] = newNode
            
            copyIt = copyIt.next
            prevCopy = newNode
            originalIt = originalIt.next

        copyIt = dummy.next
        while copyIt:
            copyIt.random = old_to_new[copyIt.random] if copyIt.random else None
            copyIt = copyIt.next

        return dummy.next