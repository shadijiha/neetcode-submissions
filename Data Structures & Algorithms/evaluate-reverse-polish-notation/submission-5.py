class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["*", "/", "+", "-"]:
                # pop top 2 elements from stack, if not enough elements raise exception
                if len(stack) < 2:
                    raise Exception("Invalid tokens")

                left, right = int(stack.pop()), int(stack.pop())
                result = 0
                if token == "+":    result = left + right
                if token == "-":    result = right - left
                if token == "*":    result = left * right
                if token == "/":    result = int(right / left)
                stack.append(result)
            else:
                stack.append(token)
        
        return int(stack.pop())