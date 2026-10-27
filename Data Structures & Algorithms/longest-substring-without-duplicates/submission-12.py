class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a set seen
        # Create a best counter to track length of longest substring
        # Create a left pointer at 0

        # For right pointer starting at index 0 of string s
            # While s[right] in seen
                # Remove s[left]
                # Increment left by 1
            # Increment best
            # Calculate best length
        # Return best length
        seen = set()
        best = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best = max(best, right - left + 1)
        return best
