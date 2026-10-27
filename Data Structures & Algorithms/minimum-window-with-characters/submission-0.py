class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # "XYZ"
        # "OUZODYXAZV"
        #       ^^ 
        #

        need = collections.Counter(t)
        missing = len(t)

        resL, resR, resLength = -1, -1, math.inf
        l, r = 0, 0

        while r < len(s):
            char = s[r]
            if need[char] > 0:
                missing -= 1
            
            need[char] -= 1

            while missing == 0:
                newLen = r - l + 1
                if newLen < resLength:
                    resL, resR, resLength = l, r, newLen
                
                left_ptr_char = s[l]
                l += 1
                if left_ptr_char in need:
                    need[left_ptr_char] += 1
                
                if need[left_ptr_char] > 0:
                    missing += 1
            r += 1
        
        return s[resL:resR+1] if resLength != math.inf else ""
                