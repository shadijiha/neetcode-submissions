class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        MAX_HEAP_MODIFIER = -1

        heap = []
        for tup in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if tup[0] < 0:
                heapq.heappush(heap, tup)

        result = []
        q = deque([])

        while heap:
            count, char = heapq.heappop(heap)
            count = MAX_HEAP_MODIFIER * count

            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                q.append((
                    count, char # importatn don't decrement the count
                ))
            else:
                result.append(char)
                count -= 1
                if count > 0:
                    heapq.heappush(heap, (MAX_HEAP_MODIFIER * count, char))

                # release all chars in the queue beceause we broke the chain with a new char
                while q:
                    q_count, q_char = q.popleft()
                    if q_count > 0:
                        heapq.heappush(heap, (MAX_HEAP_MODIFIER * q_count, q_char))

        return "".join(result)
        
            
            

            
        

        