class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in pairs:
                # closing bracket: check for a match
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                # opening bracket: push onto stack
                stack.append(char)

        return not stack