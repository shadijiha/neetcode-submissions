# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Get the midpoint
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Split the list
        secondList = slow.next
        slow.next = None

        # Now slow is at midpoint, we reverse everything slow
        reversedList = self.reverseList(secondList)

        # Rearrange
        startIt = head
        reversedListIt = reversedList
        while reversedListIt:
            reverseTempNext = reversedListIt.next
            firstHalfTempNext = startIt.next
            startIt.next = reversedListIt
            reversedListIt.next = firstHalfTempNext

            reversedListIt = reverseTempNext
            startIt = firstHalfTempNext
    
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        it = head
        while it:
            tempNext = it.next
            it.next = prev
            prev = it
            it = tempNext
        return prev
    
    def printList(self, head: Optional[ListNode]):
        it = head
        while it:
            print(it.val)
            it = it.next