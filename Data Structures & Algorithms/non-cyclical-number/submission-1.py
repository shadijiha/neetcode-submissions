class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            s = str(n)
            digits = list(s)
            summ = sum(int(d)**2 for d in digits)
            
            if summ in seen:
                return False
            if summ == 1:
                return True
            seen.add(summ)
            n = summ
        return False