class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums): # For each number in nums
            complement = target - num # Calculate the complement
            if complement in seen: # If the complement is in the dictionary
                # return [dictionary[complement], dictionary[num]]
                return [seen.get(complement), i]
            else:
                seen[num] = i # Add KV pair (i.e. 4:0, 5:1, 6:2)
        return []