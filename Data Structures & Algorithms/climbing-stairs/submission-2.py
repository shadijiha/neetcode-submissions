class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prevTwo = 1, 1

        for i in range(n - 1):
            temp = prev
            prev += prevTwo
            prevTwo = temp
        
        return prev