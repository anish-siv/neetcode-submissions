class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        result = {}  # key: tuple of counts, value: list of strings
        
        for s in strs: # Loop though all words in strs list
            count = [0] * 26 # 1. build the count array for s
            for c in s:
                count[ord(c) - ord('a')] += 1 # increment count at the right index
            
            key = tuple(count) # 2. convert to tuple
                
            result.setdefault(key, []).append(s) # 3. add s to result[key], creating the list if needed
            
        return list(result.values())