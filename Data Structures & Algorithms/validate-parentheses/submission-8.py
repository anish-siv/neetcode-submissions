class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Create empty stack
        pairs = {')': '(', '}': '{', ']': '['} # Dictionary containing bracket KV pairs

        for char in s: # Loop through every char in s
            if char == '(' or char == '{' or char == '[': # If open bracket, push to stack
                stack.append(char)
            elif char == ')' or char == '}' or char == ']': # Else if close bracket, 
                if not stack: # If the stack is empty, return false
                    return False
                if pairs[char] != stack.pop(): # If the char in pairs is not equal to the top element in stack
                    return False
        return not stack    
        
                    