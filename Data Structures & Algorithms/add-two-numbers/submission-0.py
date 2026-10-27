# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 999
        # 1
        # 0001
        # O(max(n, m)) time
        # O(max(n, m) + 1) space

        dummy = ListNode(0, None)
        resIt = dummy
        
        l1It = l1
        l2It = l2

        carry = 0
        while l1It or l2It or carry > 0:
            val1 = l1It.val if l1It else 0
            val2 = l2It.val if l2It else 0

            res = val1 + val2 + carry
            
            if res > 9:
                carry = res // 10
                res = res % 10
            else:
                carry = 0
                
            resIt.next = ListNode(res)
            
            resIt = resIt.next
            l1It = l1It.next if l1It else None
            l2It = l2It.next if l2It else None

        return dummy.next
