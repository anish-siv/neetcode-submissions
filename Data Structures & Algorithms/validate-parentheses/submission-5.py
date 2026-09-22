class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'} # Key : Value pairs
        stack = [] # Create empty stack

        for char in s: # For every char in string s
            if char in pairs: # If the char (Key - close brackets) is in pairs
                # closing bracket: check for a match
                if not stack or stack.pop() != pairs[char]: # If the stack is empty or the char does not equal the Value in pairs
                    return False # return false
            else:
                # opening bracket: push onto stack
                stack.append(char) # Add the open bracket chars into the stack

        return not stack # Return "not stack" to check whether the stack is truly empty