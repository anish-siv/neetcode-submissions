class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a dict counts (Key = Characters in the strings : Value = Number of times they appear)

        # If the length of s != length of t
            # return False
        
        # For each char in s
            # Increase the count of a char when it appears
        
        # For each char in t
            # Decrease the count of a char when it appears
        
        # For count in counts
            # If the count != 0
                # return False
        # return True

        counts = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        for char in t:
            counts[char] = counts.get(char, 0) - 1

        for count in counts.values():
            if count != 0:
                return False
        return True
