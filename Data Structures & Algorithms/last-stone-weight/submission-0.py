class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        MAX_HEAP_MODIFIER = -1

        heap = [MAX_HEAP_MODIFIER * s for s in stones] # max heap
        heapq.heapify(heap)

        while len(heap) > 1:
            top1 = heapq.heappop(heap) * MAX_HEAP_MODIFIER
            top2 = heapq.heappop(heap) * MAX_HEAP_MODIFIER

            if top1 == top2:
                continue
            else:
                newWeight = abs(top1 - top2)
                heapq.heappush(heap, newWeight * MAX_HEAP_MODIFIER)
        
        return MAX_HEAP_MODIFIER * heap[0] if len(heap) == 1 else 0
        
