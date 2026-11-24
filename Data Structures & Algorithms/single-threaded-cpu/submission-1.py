class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = [] # time, index

        processed = set()
        result = []

        time = min(start for start, _ in tasks)
        while len(result) < len(tasks):
            
            for i, [task_start, task_time] in enumerate(tasks):
                if i not in processed and time >= task_start:
                    processed.add(i)
                    heapq.heappush(heap, (task_time, i))

            if heap:
                task_time, index = heapq.heappop(heap)
                result.append(index)
                time += task_time
            else:
                time = min(start for i, [start, _] in enumerate(tasks) if i not in processed)

        return result