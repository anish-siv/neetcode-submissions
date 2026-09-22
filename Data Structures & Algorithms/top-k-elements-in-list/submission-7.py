class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Create an empty set called count
        for num in nums: # For every number in list nums
            if num in count: # If the number is in set count
                count[num] += 1 # Increment count by 1
            else:
                count[num] = 1 # Else leave it as 1

         # Sort the items in count as a list
        sorted_count = sorted(list(count.items()), key=lambda pair: pair[1], reverse=True)

        return [pair[0] for pair in sorted_count[:k]]



