class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mult = 1
        num = 0

        for d in reversed(digits):
            num += d * mult
            mult *= 10
        
        return [int(d) for d in list(str(num + 1)) ]
        
        