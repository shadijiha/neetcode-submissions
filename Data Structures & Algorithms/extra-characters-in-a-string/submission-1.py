class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #
        #                       *
        #               n              -
        #          e        -              e
        #       e               -
        #   t
        #
        dictionary = set(dictionary)

        memo = {}
        def backtrack(i, cumalative_skipped) -> int:
            if i >= len(s):
                memo[(i, cumalative_skipped)] = cumalative_skipped
                return memo[(i, cumalative_skipped)]
            
            if (i, cumalative_skipped) in memo:
                return memo[(i, cumalative_skipped)]

            res = math.inf
            for j in range(i, len(s)):
                temp = s[i:j+1]

                if temp in dictionary:
                    res = min(res, backtrack(j + 1, cumalative_skipped))
                else:
                    res = min(res, backtrack(i + 1, cumalative_skipped + 1))

            memo[(i, cumalative_skipped)] = res
            return memo[(i, cumalative_skipped)]
    
        return backtrack(0, 0)
            
