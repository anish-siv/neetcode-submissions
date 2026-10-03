class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if not lowercase[left].isalnum():
                left += 1
            elif not lowercase[right].isalnum():
                right -= 1
            else: 
                if lowercase[left] == lowercase[right]:
                    left += 1
                    right -= 1
                else:
                    return False
        return True
            

