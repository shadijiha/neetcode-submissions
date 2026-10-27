class ListNode:
    def __init__(self, val=None, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return f"{{{self.key}={self.val}}}"

class LRUCache:

    def __init__(self, capacity: int):
        self.mapToList = {}

        tail = ListNode()
        self.dummyHead = ListNode(next=tail)
        assert self.dummyHead.next == tail
        tail.prev = self.dummyHead

        self.dummyTail = tail
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.mapToList:
            return -1
        
        self.updateRecency(key)
        return self.mapToList[key].val
        
    def put(self, key: int, value: int) -> None:
        # If we're updateing
        if key in self.mapToList:
            self.mapToList[key].val = value

            # Put it at the head of the list
            self.updateRecency(key)
            return

        if len(self.mapToList) >= self.capacity:
            self._evictLRU()

        node = ListNode(value, key)
        node.next = self.dummyHead.next
        self.dummyHead.next = node
        node.prev = self.dummyHead
        node.next.prev = node
        
        self.mapToList[key] = node
    
    def _evictLRU(self):
        # Evict tail
        nodeToEvict = self.dummyTail.prev
        keyToEvict = nodeToEvict.key
        
        toEvictPreviousNode = nodeToEvict.prev
        self.dummyTail.prev = toEvictPreviousNode
        toEvictPreviousNode.next = self.dummyTail

        del self.mapToList[keyToEvict]
        
    def updateRecency(self, key):
        toMove = self.mapToList[key]

        # Update its previous
        if toMove.prev:
            toMove.prev.next = toMove.next
        
        # update the prev of the next
        if toMove.next:
            toMove.next.prev = toMove.prev
        
        # put it at the head
        currentHead = self.dummyHead.next
        self.dummyHead.next = toMove
        toMove.prev = self.dummyHead
        toMove.next = currentHead
        currentHead.prev = toMove

