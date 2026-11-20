class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        //this->heap = {nums.begin(), nums.end()};
        for (auto n : nums) {
            this->add(n);
        }
    }
    
    int add(int val) {
        if (heap.size() < k) {
            heap.push(val);
            return heap.top();
        }

        if (val > heap.top()) {
            heap.pop();
            heap.push(val);
        }

        return heap.top();
    }

private:
    int k = 0;
    std::priority_queue<int, std::vector<int>, std::greater<int>> heap;
};
