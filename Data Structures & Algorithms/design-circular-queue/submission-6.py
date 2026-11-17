class ListNode:
    def __init__(self, value, nextt=None):
        self.val = value
        self.next = nextt

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail

        self.insertion_point = self.head
        
    def enQueue(self, value: int) -> bool:
        if self.size + 1 > self.capacity:
            return False
        self.insertion_point.next = ListNode(value, self.tail)
        self.insertion_point = self.insertion_point.next
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next = self.head.next.next
        self.size -= 1

        if self.size == 0:
            self.insertion_point = self.head

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.insertion_point.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()