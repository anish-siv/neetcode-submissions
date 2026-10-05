class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Create an empty set
        for num in nums: # For every number in nums
            if num in seen: # If the number is in set seen
                return True; # Return true
            else:
                seen.add(num) # Else add number to set seen
        return False # Return false if no duplicates are found in nums