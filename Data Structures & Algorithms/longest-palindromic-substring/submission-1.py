class Solution:
    def longestPalindrome(self, s: str) -> str:
        #
        # let dp[i] be the longest palindrom until s[i]
        #. in = [(0,0), (0,0), (0,2), (0,2),(0,2)]
        #. dp = [1, 1, 3, 3, 3]
        #. s = "ababd"
        #.      ^^
        bestStart = 0
        bestEnd = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l = j - i + 1

                if l > (bestEnd - bestStart + 1) and self.isPalindrom(s, i, j):
                    bestStart = i
                    bestEnd = j
        
        return s[bestStart:bestEnd+1]


    
    def isPalindrom(self, string, start, endInclusive):
        return string[start:endInclusive+1] == string[start:endInclusive+1][::-1]