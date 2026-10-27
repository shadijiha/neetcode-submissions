class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #
        # 
        #
        freq = collections.Counter(s)
        curr_window_freq = collections.defaultdict(int)
        res = []

        l = r = 0
        while r < len(s):
            char = s[r]
            curr_window_freq[char] += 1

            # Check if I have consumed a given charcter inside my window
            found_answer = True
            for in_window_char in curr_window_freq:
                if freq[in_window_char] != curr_window_freq[in_window_char]:
                    found_answer = False
                    break
            
            if found_answer:
                res.append(r - l + 1)
                curr_window_freq.clear()
                l = r + 1
            r += 1
        return res