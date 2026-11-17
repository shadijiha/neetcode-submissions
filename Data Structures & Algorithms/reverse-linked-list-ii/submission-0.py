# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        it = dummy
        position = 0

        detach_left, detach_right = None, None

        while it:
            if position == left - 1:
                detach_left = it
            elif position == right:
                detach_right = it
            it = it.next
            position += 1

        # detach
        detached_head = detach_left.next
        detached_tail_section = detach_right.next
        detach_right.next = None

        # attach tail to first section
        reversed_head, reversed_tail = self._reverse_list(detached_head)

        detach_left.next = reversed_head
        reversed_tail.next = detached_tail_section

        return dummy.next

    def _reverse_list(self, list1) -> (ListNode, ListNode):
        prev, current = None, list1
        while current:
            nextt = current.next
            current.next = prev
            prev = current
            current = nextt

        return prev, list1