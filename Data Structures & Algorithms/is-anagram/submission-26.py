class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1 # If the char isn't in counts, default to 0 and add 1
        
        for char in t:
            counts[char] = counts.get(char, 0) - 1 # If the char isn't in counts, default to 0 and subtract 1
            if counts[char] < 0:
                return False

        return True
    

