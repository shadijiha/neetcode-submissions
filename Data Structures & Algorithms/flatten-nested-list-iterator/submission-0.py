class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()
        

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True
            
            # Consume the list
            self.stack.pop()

            for e in reversed(top.getList()):
                self.stack.append(e)
        return False
        
        
        
        
