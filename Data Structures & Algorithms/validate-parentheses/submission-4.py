class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '{' or c == '(' or c == "[":
                stack.append(c)
            
            if len(stack) == 0:
                return False
            
            top = stack[-1]
            if c == '}':
                if top == '{':
                    stack.pop()
                else:
                    stack.append(c)

            if c == ')':
                if top == '(':
                    stack.pop()
                else:
                    stack.append(c)
            if c == ']':
                if top == '[':
                    stack.pop()
                else:
                    stack.append(c)

        
        return len(stack) == 0