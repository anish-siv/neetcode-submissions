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
        # For every character in string s
            # Check if each character is in pairs
                # If the stack is not empty or the popped character from the stack != value of the current character from pairs
                    # Return false
                # Else
                    # Push the character to the stack
            # Return true if stack is empty at the end    
