class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)
        heap = [(count, char) for char, count in freq_map.items()]
        heapq.heapify_max(heap)

        result = []
        q = deque()
        while heap or q:
            freq, char = 0, None
            
            if heap:
                freq, char = heapq.heappop_max(heap)
                        
            if char is not None:
                result.append(char)
                freq -= 1

            # empty the queue
            while q:
                temp_freq, temp_char  = q.popleft()
                heapq.heappush_max(heap, (temp_freq, temp_char))

            # add this iteration char to queue
            if freq > 0:
                q.append((freq, char))
            
            if not q and len(heap) == 1 and heap[0][0] > 1:
                return ""
        
        return "".join(result)
