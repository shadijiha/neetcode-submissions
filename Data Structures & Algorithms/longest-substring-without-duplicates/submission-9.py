class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_freq = {} # char: index
        maxx = 0

        l, r = 0, 0

        while r < len(s):
            char = s[r]

            if char in window_freq:
                index = window_freq[char]           
                #l = index + 1

                while l <= index:
                    if s[l] in window_freq:
                        del window_freq[s[l]]
                    l += 1

                # new_window = {}
                # for key in window_freq:
                #     if window_freq[key] >= index:
                #         new_window[key] = index
                # window_freq = new_window
            else:
                maxx = max(maxx, r - l + 1)
            window_freq[char] = r        
            r += 1

        return maxx