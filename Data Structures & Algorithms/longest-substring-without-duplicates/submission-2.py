class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        seen = set()
        l = 0
        res = -math.inf

        for r in range(len(s)):
            c = s[r]

            while c in seen:
                res = max(res, r - l)
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

        res = max(res, r - l + 1)
        return res
            
            
                