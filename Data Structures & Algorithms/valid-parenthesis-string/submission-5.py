class Solution:
    def checkValidString(self, s: str) -> bool:
        para = []
        wildcards = []

        for i, c in enumerate(s):
            if c == "(":
                para.append(i)
            elif c == "*":
                wildcards.append(i)
            elif c == ")":
                if len(para) > 0:
                    para.pop()
                elif len(wildcards) > 0:
                    wildcards.pop()
                else:
                    return False
        
        while para and wildcards:
            if para.pop() > wildcards.pop():
                return False

        return len(para) == 0
