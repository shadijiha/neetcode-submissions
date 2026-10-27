class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMax = leftMax - 1
                leftMin = leftMin - 1
            elif c == "*":
                leftMax = leftMax + 1
                leftMin = leftMin - 1

            if leftMax < 0:
                return False
            leftMin = max(leftMin, 0)

        return leftMin == 0

