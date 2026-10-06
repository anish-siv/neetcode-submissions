class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums: # For each number in nums
            freq[num] = freq.get(num, 0) + 1  # Get the frequency of each number's appearance in nums 
            # rev_values = list(freq.values())
        return sorted(freq, key=freq.get, reverse=True)[:k]


