class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        MIN = -2147483648

        res = 0
        while x != 0:
            # Chop the right most digit from the arg x
            digit = int(math.fmod(x, 10))      # can't use % with negative numbers in python

            # Mutate the same x arg because we want to move on to reverse digit
            x = int(x / 10)               # can't use // with negative numbers in python

            if (res > MAX // 10) or \
                (res == MAX // 10 and digit > (MAX % 10)):
                return 0
            
            if (res < MIN // 10) or \
                (res == MIN // 10 and digit < (MIN % 10)):
                return 0
            
            res = (res * 10) + digit
        
        return res
