class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create a dict freq (Key = Character in string : Value = # of times it appears in string)
        # Create a left pointer
        # Create a maxF variable
        # Create a best variable

        # For each right from 0 to end of the string
            # Increase the count of the character at the right pointer into the dict
            # maxF is the max valuee between maxF and the value of s[right] in freq
            # If window length - maxF > k
                # Remove s[left] from freq
                # Increment left by 1

        freq = {}
        left = 0
        maxF = 0
        best = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxF = max(maxF, freq[s[right]])
            if (right - left + 1) - maxF > k:
                freq[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best