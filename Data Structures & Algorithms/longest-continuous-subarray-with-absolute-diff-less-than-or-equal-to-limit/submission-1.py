class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # arr [7, 2, 3, 6]
        #         ^     ^
        # max_q = [0, 3] indicies instead values --> [7, 6]
        # min_q = [2, 3, 4, 5]   
        # O(n)
        # O(n)

        maxQ = deque()
        minQ = deque()

        maxSubarray = 0

        l = r = 0

        while r < len(nums):

            # make sure the maxQ is descending order
            num = nums[r]
            while maxQ and num > nums[maxQ[-1]]:
                maxQ.pop()
            
            while minQ and num < nums[minQ[-1]]:
                minQ.pop()
            
            maxQ.append(r)
            minQ.append(r)

            # top of the queue is in my window          
            if l > maxQ[0]:
                maxQ.popleft()
            if l > minQ[0]:
                minQ.popleft()

            while maxQ and minQ and abs(nums[maxQ[0]] - nums[minQ[0]]) > limit:
                l += 1
                if l > maxQ[0]:
                    maxQ.popleft()
                if l > minQ[0]:
                    minQ.popleft()
                
            maxSubarray = max(maxSubarray, r - l + 1)
            r += 1

        return maxSubarray

