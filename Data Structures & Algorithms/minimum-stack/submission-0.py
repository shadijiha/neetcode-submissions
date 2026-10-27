class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
