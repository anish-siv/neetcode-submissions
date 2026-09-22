class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1]: # If min_stack is empty or the new value < min_stack's top value
            self.min_stack.append(val) # Append the new val as the minimum in min_stack
        else:
            self.min_stack.append(self.min_stack[-1]) # Re-append the same minimum value at top of stack

    def pop(self) -> None:
        self.stack.pop() # Pop top value from stack
        self.min_stack.pop() # Pop top value from min_stack

    def top(self) -> int:
        return self.stack[-1] # Return top value from the stack

    def getMin(self) -> int:
        return self.min_stack[-1] # Return the minimum value of the stack
