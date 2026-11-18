class ListNode:
    def __init__(self, key: int, val: int, nextt=None, prev=None):
        self.val = val
        self.next = nextt
        self.prev = prev
        self.key = key

class LRUCache:
    def __init__(self):
        """
            LRU has infinit capacity, because LFU will handle capacity mangement
        """
        self.head = ListNode(None, 0)
        self.tail = ListNode(None, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {} # key: ListNode O(1) access
    
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        self._update_recency(key)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self._update_recency(key)
            return
        
        node = ListNode(key, value)
        self.map[key] = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        #self._update_recency(key)
        return

    def size(self) -> int:
        return len(self.map)

    def remove(self, key: int):
        if key not in self.map:
            return
        
        node = self.map[key]

        # rewise the list
        node_next = node.next
        node_prev = node.prev

        node_prev.next = node_next
        node_next.prev = node_prev

        del self.map[key]

    def _update_recency(self, key: int) -> None:
        if key not in self.map:
            return
        
        node = self.map[key]
        node_next = node.next
        node_prev = node.prev

        # rewise where node was removed
        node_next.prev = node_prev
        node_prev.next = node_next

        # wire node to the head of the recency list
        head_next = self.head.next
        self.head.next = node
        node.next = head_next
        head_next.prev = node
        node.prev = self.head

    def remove_least_recent(self) -> int:
        if self.size() == 0:
            return None

        # tail.prev
        node = self.tail.prev
        self.remove(node.key)
        return node.key

class LFUCache:

    def __init__(self, capacity: int):
        self.keys = {} # key: frequency
        self.map = {} # frequency: LRUCache
        self.min_freq = 0 # I want to know from which LRU to delete when eviciting
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        freq = self.keys[key]
        new_freq = freq + 1

        # delete from freq LRU
        value = self.map[freq].get(key)
        self.map[freq].remove(key)
        if self.map[freq].size() == 0:
            if self.min_freq == freq:
                self.min_freq = new_freq
            del self.map[freq]
        
        # add it to new_freq LRU
        if new_freq not in self.map:
            self.map[new_freq] = LRUCache()
        
        self.map[new_freq].put(key, value)
        self.keys[key] = new_freq
        return value       

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return True

        if key in self.keys:
            self.get(key)
            freq = self.keys[key]
            cache = self.map[freq]
            cache.put(key, value)
            return

        if self.is_full():
            # evict the lowest freq
            evicted_key = self.map[self.min_freq].remove_least_recent()
            del self.keys[evicted_key]
            self.size -= 1

        freq = 1
        if freq not in self.map:
            self.map[freq] = LRUCache()
        self.min_freq = freq

        self.keys[key] = freq
        self.map[freq].put(key, value)
        self.size += 1
    
    def is_full(self):
        return self.size >= self.capacity
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)