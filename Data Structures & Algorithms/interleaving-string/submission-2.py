class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #
        # s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"
        #       ^            ^            ^
        #   backtrack(i+1, j, k+1)  
        #                          
        #   backtrack(i, j + 1, k+1)  

        #   backtrack(i, j+1, k+1)   oR backtrack(i+1, j, k+1)
        # 
        memo = {}
        def backtrack(i, j, k) -> bool:
            if len(s1) + len(s2) != len(s3):
                return False
            if k >= len(s3):
                return True
            
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            letter_s1 = s1[i] if i < len(s1) else ""
            letter_s2 = s2[j] if j < len(s2) else ""
            letter_s3 = s3[k]

            result = False
            if letter_s1 != letter_s2 and letter_s1 == letter_s3:
                result = backtrack(i + 1, j, k + 1)
            elif letter_s1 != letter_s2 and letter_s2 == letter_s3:
                result = backtrack(i, j + 1, k + 1)
            elif letter_s1 == letter_s2 and letter_s1 == letter_s3:
                result = backtrack(i + 1, j, k + 1) or backtrack(i, j + 1, k + 1)
            
            memo[(i, j, k)] = result
            return memo[(i, j, k)]
        
        return backtrack(0, 0, 0)