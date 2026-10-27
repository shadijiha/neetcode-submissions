class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 2
        # 
        #            (                  
        #     )           (
        #  (            )
        #  )            )

        res = []
        sol = []

        def backtrack(open_count=0, closed_count=0):
            if open_count == n and closed_count == n:
                res.append("".join(sol))
                return
            
            if open_count == closed_count:
                sol.append("(")
                backtrack(open_count + 1, closed_count)   
                sol.pop()
            
            if open_count > closed_count and open_count < n:
                sol.append("(")
                backtrack(open_count + 1, closed_count)   
                sol.pop()
            
            if closed_count < open_count:
                sol.append(")")
                backtrack(open_count, closed_count + 1)   
                sol.pop()


        backtrack()
        return res
