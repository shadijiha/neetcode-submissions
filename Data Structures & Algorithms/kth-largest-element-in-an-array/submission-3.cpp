class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> heap;

        for (int n : nums) {
            if (heap.size() < k) {
                heap.push(n);
                continue;
            }

            if (n > heap.top()) {
                heap.pop();
                heap.push(n);
            }
        }

        return heap.top();
    }
};
