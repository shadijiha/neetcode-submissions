class Solution:
    def countSubstrings(self, s: str) -> int:
        #
        # let dp[i][j] be True if string from i to j+1 is a palindrom
        #     dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1] 
        #
        #.  "aabac"
        #.     ^

        count = 0
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    count += 1
                    dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])

        return count