class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith("0"):
            return 0
        
        cache = { len(s): 1 }

        def dfs(i):
            if i in cache:
                return cache[i]
            
            c = s[i]
            c2 = s[i:i+2] if i + 1 < len(s) else ""
            
            res = 0
            if c != "0":
                res += dfs(i + 1)
            if c2 != "" and int(c2) < 27 and int(c2) >= 10:
                res += dfs(i + 2)
            cache[i] = res
            return res
        
        return dfs(0)
