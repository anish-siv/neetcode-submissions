class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return not stack

        # For every char in s
            # If the char is in pairs
                # If stack is not empty or popped char from stack != value in pairs key
                    # Return false
            # Else
                # Push the open char into stack
        # Return True if stack is empty at the end (so we know it is valid parentheses sequence)
