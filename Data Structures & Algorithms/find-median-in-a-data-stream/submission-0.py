MAX_HEAP_MODIFIER = -1
class MedianFinder:
    

    def __init__(self):
        # [1, 2, 3, 4]
        self.left, self.right = [], []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, MAX_HEAP_MODIFIER * num)

        # are all elements from left less than right
        if len(self.right) > 0 and len(self.left) > 0 and \
           (MAX_HEAP_MODIFIER * self.left[0]) > self.right[0]:
            val = MAX_HEAP_MODIFIER * heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        
        # if heaps are unbalanced
        if len(self.left) >= len(self.right) + 2:
            val = MAX_HEAP_MODIFIER * heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        
        if len(self.right) >= len(self.left) + 2:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, MAX_HEAP_MODIFIER * val)
        
    def findMedian(self) -> float:
        if len(self.left) != len(self.right):
            if len(self.left) > len(self.right):
                return MAX_HEAP_MODIFIER * self.left[0]
            else:
                return self.right[0]
        else:
            return (self.right[0] + MAX_HEAP_MODIFIER * self.left[0]) / 2
        
        