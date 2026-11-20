class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap of size k
        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
                continue
            
            if n > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, n)

        return heap[0]
