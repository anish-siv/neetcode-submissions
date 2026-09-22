class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack: # If empty, push current val into min_stack
            return self.min_stack.append(val)
        elif val < self.min_stack[-1]: # Else if val is < min_stack
            return self.min_stack.append(val)
        else:
            return self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
