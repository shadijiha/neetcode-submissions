class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1 if n % 2 != 0 else 0
            n = n >> 1
        
        return res