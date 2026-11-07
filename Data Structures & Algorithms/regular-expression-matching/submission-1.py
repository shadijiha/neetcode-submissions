class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}

        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True

            if j >= len(p):
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            # is the next char in pattern a "*"? 
            # always j + 1 because * can never be the first ever char
            if j + 1 < len(p) and p[j + 1] == "*":
                if dfs(i, j + 2):  # don't use it
                    memo[(i, j)] = True
                    return True
                
                # Use it only if there's a match between s and p
                if match and dfs(i + 1, j):
                    memo[(i, j)] = True
                    return True
            
            # advance both pointers
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return False
        
        return dfs(0, 0)
