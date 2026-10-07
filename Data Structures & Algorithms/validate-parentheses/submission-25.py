class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return not stack

        # For each character in the string
            # If the stack is not empty or stack.pop is not equal to pairs[char] (Value of the Key)
                # Return False
            # Else
                # Push the character to the stack (open char)
        # Return True if stack is empty







# Edge case: Close bracket starts the string first