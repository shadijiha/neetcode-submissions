# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visisted_nodes = set()

        it = head
        while it is not None:
            if it in visisted_nodes:
                return True
            visisted_nodes.add(it)
            it = it.next
        return False