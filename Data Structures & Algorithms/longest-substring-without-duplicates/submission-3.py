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
                # no + 1 here because we already passed the actual result (r - 1) is the last index without repeating
                res = max(res, r - l)
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

        # here we need +1 because what if the entire string is unique
        # the +1 is needed because indicies are 0 based 
        res = max(res, r - l + 1)
        return res
            
            
                