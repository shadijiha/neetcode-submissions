class Solution:
    def reverseBits(self, n: int) -> int:
        BITS = 32
        ZERO_INDEXED_BITS = BITS - 1

        res = 0

        for i in range(BITS):
            bit = (n >> i) & 1
            res = res | (bit << (ZERO_INDEXED_BITS - i))
        return res