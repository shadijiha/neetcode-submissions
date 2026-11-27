class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        longest = None

        for i in range(len(strs) - 1):
            current = strs[i]
            nextt = strs[i + 1]

            j = 0
            while j < min(len(current), len(nextt)) and current[j] == nextt[j]:
                j += 1

            tmp = current[:j]

            if longest is None or len(tmp) < len(longest):
                longest = tmp

        return longest