# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        
        position = 0
        it1 = list1
        while it1:
            if position == a - 1:
                break
            it1 = it1.next
            position += 1
        
        # I am at detachement point
        detached_section = it1.next
        it1.next = list2

        while detached_section:
            if position == b:
                break
            detached_section = detached_section.next
            position += 1
        
        # Attach rest to list 2
        it2 = list2
        while it2.next:
            it2 = it2.next
        it2.next = detached_section

        return list1