# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        remaininglength = self.listLength(head)

        firstReverse = None
        previousSectionTail = None

        it = head
        while remaininglength >= k:
            newHead, newTail, nextSection = self.reverseList(it, k)

            if firstReverse is None: 
                firstReverse = newHead
            
            newTail.next = nextSection
            if previousSectionTail:
                previousSectionTail.next = newHead

            it = nextSection
            previousSectionTail = newTail
            remaininglength -= k
            
        
        return firstReverse if firstReverse else head
    
    def reverseList(self, head: Optional[ListNode], k: int) -> Tuple[ListNode, ListNode, ListNode]:
        originalHead = head
        nextSection = None
        it = head
        prev = None
        while it and k > 0:
            tmpNext = it.next
            it.next = prev
            prev = it            
            it = tmpNext
            nextSection = tmpNext
            k -= 1
        
        return prev, originalHead, nextSection

    
    def listLength(self, head: Optional[ListNode]) -> int:
        it = head
        length = 0
        while it:
            length += 1
            it = it.next
        return length