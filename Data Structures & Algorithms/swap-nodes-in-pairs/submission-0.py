# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [d,4,7,2,9]
        #  ^
        dummy = ListNode(0, head)

        it = dummy
        while it and it.next:
            print(it.val)
            temp = it.next
            it.next = it.next.next

            if it.next: 
                temp2 = it.next.next
                it.next.next = temp
                temp.next = temp2
            else:
                it.next = temp
            it = temp
        return dummy.next    
    
