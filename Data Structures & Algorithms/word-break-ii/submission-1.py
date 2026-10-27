class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        res = []

        def dfs(i, sol):
            if i >= len(s):
                res.append(" ".join(sol))
            
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr in wordDict:
                    sol.append(substr)
                    dfs(j + 1, sol)
                    sol.pop()

        dfs(0, [])
        return res


