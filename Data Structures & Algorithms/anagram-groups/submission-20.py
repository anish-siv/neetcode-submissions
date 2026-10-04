class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # Create empty dictionary called groups
        for i in range(len(strs)): # Loop though all words in strs
            key = "".join(sorted(strs[i])) # Create key by sorting each word's characters in alpha order
            groups.setdefault(key, []).append(strs[i]) # If the key doesn't exist in groups yet, give default [], and append word
        return list(groups.values())


# Input: ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }