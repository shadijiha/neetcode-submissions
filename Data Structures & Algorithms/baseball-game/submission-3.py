class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if self._is_digit(op):
                scores.append(int(op))
            elif op == "+":
                if len(scores) < 2:
                    raise Exception()
                
                s1 = scores[-1]
                s2 = scores[-2]

                scores.append(s1 + s2)
            elif op == "D":
                if len(scores) < 1: continue
                scores.append(scores[-1] * 2)
            elif op == "C":
                scores.pop()
            print(scores)

        return sum(scores)

    def _is_digit(self, s: str) -> bool:
        try:
            n = int(s)
            return True
        except:
            return False