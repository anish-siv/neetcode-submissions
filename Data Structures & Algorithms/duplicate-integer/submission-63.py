class Solution: 
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a set seen

        # For each num in nums
            # If num in seen
                # return True
            # Else
                # Add num to seen
        # return False

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False