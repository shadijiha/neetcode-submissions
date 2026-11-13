class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        n_2th = 0
        n_1th = 1
        n_th = 1

        for i in range(2, n):
            temp = n_th
            n_th = n_th + n_1th + n_2th

            n_2th = n_1th
            n_1th = temp

        return n_th