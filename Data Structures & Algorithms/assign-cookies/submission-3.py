class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        happy = 0
        cookie_index = 0

        for i in range(len(g)):
            while cookie_index < len(s) and g[i] > s[cookie_index]:
                cookie_index += 1
            if cookie_index >= len(s):  break

            if s[cookie_index] >= g[i]:
                happy += 1
                cookie_index += 1
        return happy