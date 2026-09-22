class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
            
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            end = (j+1) + length
            word = s[j+1 : end]
            result.append(word)
            i = end
        return result



        # step 1: find '#' starting from i
        # step 2: get the length
        # step 3: slice out the string
        # step 4: append to result
        # step 5: advance i