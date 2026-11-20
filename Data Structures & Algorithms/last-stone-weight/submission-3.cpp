class Solution {
public:
    int lastStoneWeight(std::vector<int>& stones) {
        std::priority_queue<int, std::vector<int>, std::less<int>> heap(stones.begin(), stones.end());

        while (heap.size() > 1) {
            int x = heap.top();
            heap.pop();
            int y = heap.top();
            heap.pop();

            int new_stone = std::abs(x - y);

            if (new_stone > 0) {
                heap.push(new_stone);
            }
        }

        return heap.empty() ? 0 : heap.top();
    }
};
