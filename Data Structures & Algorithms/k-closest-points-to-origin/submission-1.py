class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #
        # (distance, [x, y])
        #
        ORIGIN_X, ORIGIN_Y = 0, 0
        heap = []

        for p in points:
            x, y = p
            distance = math.sqrt( (x - ORIGIN_X)**2 + (y - ORIGIN_Y)**2 )
            heapq.heappush(heap, (distance, p))
        
        return [p for d, p in heapq.nsmallest(k, heap)]
