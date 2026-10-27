class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # abbc
        # lecabxbee
        #   ^  ^^    
        frequency_map = collections.Counter(s1)
        l, r = 0, 0

        window_frequency_map = frequency_map.copy()

        while r < len(s2):
            char = s2[r]
            if char not in window_frequency_map:
                l += 1 # todo double check
                r = l
                window_frequency_map = frequency_map.copy()  # TOdo optimize no need to copy if not modified
                continue

            window_frequency_map[char] -= 1
            if window_frequency_map[char] <= 0:
                del window_frequency_map[char]
            
            if len(window_frequency_map) == 0:
                return True
            r += 1
        return False
