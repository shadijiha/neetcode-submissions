class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_count = Counter(tasks)
        heap = [-n for n in task_count.values()]
        heapq.heapify(heap)

        q = deque()   # next_time, decreased_count
        time = 0
        while heap or q:

            # Check the top if the queue it is greater than time
            if q and q[0][0] < time:
                _, decreased_count = q.popleft()
                heapq.heappush(heap, -decreased_count)
            
            if heap:
                task_count = -1 * heapq.heappop(heap)
                if task_count - 1 > 0:
                    q.append(
                        (time + n, task_count - 1)
                    )
            
            time += 1

        return time