class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        
        for i in range(n + 1):
            bits_count = 0
            num = i
            while num != 0:
                bits_count += 1 if num % 2 != 0 else 0
                num = num >> 1
            res[i] = bits_count
        return res