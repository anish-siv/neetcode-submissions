class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False;
        
        charCounts = [0] * 26

        for i in range(0, len(s)):
            s_index = ord(s[i]) - ord('a')
            t_index = ord(t[i]) - ord('a')
            charCounts[s_index] += 1   # increment
            charCounts[t_index] -= 1   # decrement

        for i in range(0, len(charCounts)):
            if(charCounts[i] != 0):
                return False
        return True
