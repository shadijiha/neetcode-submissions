record Task(int enqueueTime, int processingTime, int index) {}

class Solution {
    public int[] getOrder(int[][] tasks) {
        if (tasks.length == 0) {
            return new int[0];
        }

        List<Task> sortedTasks = IntStream.range(0, tasks.length)
            .mapToObj(i -> new Task(tasks[i][0], tasks[i][1], i))
            .sorted(
                Comparator.comparingInt(Task::enqueueTime)
                    .thenComparingInt(Task::processingTime)
                    .thenComparingInt(Task::index)
            )
            .toList();
        int sortedTasksPtr = 0;

        PriorityQueue<Task> heap = new PriorityQueue<>(
            Comparator.comparingInt(Task::processingTime)
                .thenComparingInt(Task::index)
        );
        List<Integer> result = new ArrayList<>();

        int cpuTime = sortedTasks.get(sortedTasksPtr).enqueueTime();
        while (result.size() < tasks.length) {

            while (sortedTasksPtr < sortedTasks.size() &&
                cpuTime >= sortedTasks.get(sortedTasksPtr).enqueueTime() 
            ) {
                Task task = sortedTasks.get(sortedTasksPtr);
                heap.offer(task);
                sortedTasksPtr++;
            }

            if (!heap.isEmpty()) {
                Task task = heap.poll();
                result.add(task.index());
                cpuTime += task.processingTime();
            } else {
                // advance time
                cpuTime = sortedTasks.get(sortedTasksPtr).enqueueTime();
            }
        }
                
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}