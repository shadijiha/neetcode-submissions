class MyStack:

    def __init__(self):
        self.input = deque() # only allowed to use popleft
        

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        # [1, 2, 3]
        # 
        #
        temp = deque()
        while len(self.input) > 1:
            temp.append(self.input.popleft())
        
        value = self.input.popleft()
        self.input = temp
        return value

    def top(self) -> int:
        return self.input[-1]
        
    def empty(self) -> bool:
        return not self.input
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()