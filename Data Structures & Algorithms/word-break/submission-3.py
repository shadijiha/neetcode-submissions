class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP solution
        #
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in reversed(range(len(s))):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: break
    
        return dp[0]
        # Backtracking solution
        #
        
        # ["neet","code"] "neetcode"
        #                       *   
        #               neet                code
        #       neetneet    neetcode     codecode   codeneet
        #
        #
        # O(n^n)
        # O(n) with memoazation
        # cache = {}

        # def backtrack(word, sol):
        #     curSol = "".join(sol)
        #     if curSol in cache:
        #         return cache[curSol]

        #     if curSol == s:
        #         cache[curSol] = True
        #         return True
        #     if len(curSol) > len(s):
        #         cache[curSol] = False
        #         return False
            
        #     sol.append(word)
        #     for w in wordDict:
        #         if backtrack(w, sol):
        #             cache[curSol] = True
        #             return True
        #     sol.pop()

        #     return False

        # for word in wordDict:
        #     if backtrack(word, []):
        #         return True

        # return False