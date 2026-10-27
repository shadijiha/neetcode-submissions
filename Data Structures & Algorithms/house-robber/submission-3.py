class Solution:
    def rob(self, nums: List[int]) -> int:
        robArray = [0 for _ in nums]

        for i, n in enumerate(nums):
            if i == 0:
                robArray[i] = n
                continue
            elif i == 1:
                robArray[i] = max(robArray[0], n)
                continue

            maxRob = max(n + robArray[i - 2], robArray[i - 1])
            robArray[i] = maxRob
        
        return robArray[-1]