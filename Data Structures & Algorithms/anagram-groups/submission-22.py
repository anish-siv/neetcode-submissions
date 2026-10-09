class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for word in strs: # For each word in strs
            # grouped = [] # This is the list (Value of the Key in dictionary dict)
            key = "".join(sorted(word)) 
            if key not in dictionary:
                dictionary[key] = [word]
            else:
                dictionary[key].append(word)
        return list(dictionary.values())