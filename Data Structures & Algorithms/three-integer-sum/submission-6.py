class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: # If i is greater than 0 and the number at nums[i] is equal to the number before it, skip 
                continue
            left = i + 1 # Start left pointer at i+1 (as i starts at 0)
            right = len(nums) - 1 # Start right pointer at end of nums
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0: # If the three numbers are greater than 0, decrease right
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0: # If the three numbers are less than 0, increase left
                    left += 1
                else:
                    results.append((nums[i], nums[left], nums[right])) # If the numbers all add up to 0, append to results list. Increase left and decrease right to find more triplets
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: # While left is < right and the number at nums[left] is equal to the number before it, increase left pointer
                        left += 1
                    while right > left and nums[right] == nums[right + 1]: # While right is > right and the number at nums[right] is equal to the number after it, decrease right pointer
                        right -= 1
        return results 