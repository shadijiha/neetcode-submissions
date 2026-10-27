class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            1: [],
            2: list("abc"),
            3: list("def"),
            4: list("ghi"),
            5: list("jkl"),
            6: list("mno"),
            7: list("pqrs"),
            8: list("tuv"),
            9: list("wxyz"),
            0: [" "],
        }

        res = []

        def backtrack(i, sol):
            if i >= len(digits):
                if len(sol) > 0 and len(sol) == len(digits):
                    res.append("".join(sol[:]))
                return
            
            num = digits[i]
            maps_to = digits_map[int(num)] if int(num) in digits_map else []
            for c in maps_to:
                sol.append(c)
                backtrack(i + 1, sol)
                sol.pop()

                #backtrack(i + 1, sol)      
      
        backtrack(0, [])
        return res