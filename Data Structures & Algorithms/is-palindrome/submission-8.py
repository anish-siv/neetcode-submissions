class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = [char.lower() for char in s if char.isalnum()]

        left = 0
        right = len(char_list) - 1

        while left < right:
            if char_list[left] == char_list[right]:
                left += 1
                right -= 1
            else:
                return False
        return True



        
