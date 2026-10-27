class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k # 3
        # heap len should always be k or less
        self.heap = [] # 4, 5, 8

        for n in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, n)
            else:
                if n > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, n)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]

        if val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
