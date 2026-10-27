class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Need to process the most frequent task first
        #   ["A","A","B","B", "C"] n=3 min_clock=2
        #     0   4   1   5    2  
        # clock=1
        #                   next=clock+n+1
        # q= []
        # 1. Preprocess tasks, keep track of each unique task last schedule, next=last+n+1
        # answer be last + 1?
        # if task not in tacker map then min_clock, increment min_clock
        tasks = collections.Counter(tasks).most_common()

        min_clock = 0
        tasks_last_schedule = {}
        task_queue = []

        for task, frequency in tasks:
            for i in range(frequency):
                task_start_clock = 0
                if task not in tasks_last_schedule:
                    task_start_clock = min_clock
                    min_clock += 1
                else:
                    task_start_clock = tasks_last_schedule[task] + n + 1
                tasks_last_schedule[task] = task_start_clock

                heapq.heappush(task_queue, (task_start_clock, task))

        clock = 0
        while task_queue:
            top_task_start, task = task_queue[0]
            if top_task_start > clock:
                clock += 1
                continue
            
            heapq.heappop(task_queue)
            clock += 1

        return clock


