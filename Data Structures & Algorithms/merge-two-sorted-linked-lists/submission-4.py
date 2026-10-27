# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        it1 = list1
        it2 = list2

        newList = None
        headOfNewList = None

        while it1 and it2:
            if it1.val < it2.val:
                if newList is None:
                    newList = ListNode(it1.val)
                    headOfNewList = newList
                    it1 = it1.next
                    continue
                newList.next = ListNode(it1.val)
                newList = newList.next
                it1 = it1.next
            else:
                if newList is None:
                    newList = ListNode(it2.val)
                    headOfNewList = newList
                    it2 = it2.next
                    continue
                newList.next = ListNode(it2.val)
                newList = newList.next
                it2 = it2.next
        
        while it1:
            if newList is None:
                newList = ListNode(it1.val)
                headOfNewList = newList
                it1 = it1.next
                continue
            newList.next = ListNode(it1.val)
            newList = newList.next
            it1 = it1.next

        while it2:
            if newList is None:
                newList = ListNode(it2.val)
                headOfNewList = newList
                it2 = it2.next
                continue
            newList.next = ListNode(it2.val)
            newList = newList.next
            it2 = it2.next
        
        return headOfNewList