class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        result = []

        i = len(digits) - 1
        while i >= 0 or carry:
            val = digits[i] if i >= 0 else 0
            to_add = 1 if i == len(digits) - 1 else 0
            temp_res = val + to_add + carry

            if temp_res > 9:
                carry = temp_res // 10
                temp_res = temp_res % 10
            else:
                carry = 0
            
            result.append(temp_res)
            i -= 1
        
        return list(reversed(result))