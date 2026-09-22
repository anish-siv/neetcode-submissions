class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2          # how do you find the midpoint of low and high?
            
            if nums[mid] == target:
                return mid     # what do you return when you've found it?
            elif nums[mid] < target:
                low = mid + 1      # target is bigger, so which boundary moves, and to where?
            else:
                high = mid - 1     # target is smaller, so which boundary moves, and to where?
        return -1