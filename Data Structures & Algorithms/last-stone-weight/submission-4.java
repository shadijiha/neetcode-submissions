class Solution {
    public int lastStoneWeight(int[] stones) {
        List<Integer> stonesList = Arrays.stream(stones).boxed().toList();
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
        minHeap.addAll(stonesList);

        while(minHeap.size() > 1) {
            int x = minHeap.poll();
            int y = minHeap.poll();

            int res = Math.abs(y - x);
            minHeap.add(res);
        }

        return minHeap.peek();
    }
}
