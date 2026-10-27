class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAABABB k=1
        #    lr      
        # 3
        currentWindowFreq = collections.defaultdict(int)

        maxFrequency = 0
        l = r = 0
        res = 0
        while r < len(s):
            currentChar = s[r]
            currentWindowFreq[currentChar] += 1

            # what's the most frequent char in my curent window
            maxFrequency = max(maxFrequency, currentWindowFreq[currentChar])

            # if chars inside the window - the most frequent char > k
            # that means we need to shrink our window, because we can't flip all chars to make the longest string
            
            while l <= r and (r - l + 1) - maxFrequency > k:
                currentWindowFreq[s[l]] -= 1
                l += 1
            windowSize = r - l + 1
            res = max(res, windowSize)
            r += 1

        return res
        

