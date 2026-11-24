class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = [] # time, index
        sorted_tasks = sorted([(enqueue, time, i) for i, (enqueue, time) in enumerate(tasks)], key=lambda t: t[0])
        sorted_tasks_ptr = 0

        result = []
        
        time = sorted_tasks[sorted_tasks_ptr][0]
        while len(result) < len(tasks):
            
            while sorted_tasks_ptr < len(sorted_tasks) and time >= sorted_tasks[sorted_tasks_ptr][0]:
                task_start, task_time, i = sorted_tasks[sorted_tasks_ptr]
                heapq.heappush(heap, (task_time, i))
                sorted_tasks_ptr += 1
                
            if heap:
                task_time, index = heapq.heappop(heap)
                result.append(index)
                time += task_time
            else:
                time = sorted_tasks[sorted_tasks_ptr][0]

        return result