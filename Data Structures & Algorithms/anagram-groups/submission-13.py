class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} # Create empty dictionary called result

        for s in strs: # Loop through strs
            count = [0] * 26 # Create an empty count list with 26 empty spots
            for c in s: # Loop though s 
                count[ord(c) - ord('a')] += 1 # For every character c in the string, subtract by 'a' and give it a place within count

            key = tuple(count) # Covert 
            result.setdefault(key, []).append(s)

        return list(result.values())

