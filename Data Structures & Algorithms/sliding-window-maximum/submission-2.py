from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #
        # q = [4, 2, ]
        # 
        # [1,2,1,0,4,2,6]
        #          i   j

        q = deque()
        result = []

        i, j = 0, 0
        while j < len(nums):

            # pop all elements less than i
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)

            # now make sure top element is in bound of window
            if q[0] < i:
                q.popleft()
            
            if j - i + 1 >= k:
                result.append(nums[q[0]])
                i += 1
            j += 1
        return result