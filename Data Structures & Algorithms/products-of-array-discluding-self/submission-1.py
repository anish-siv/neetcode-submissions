class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1] * len(nums)
        rightProducts = [1] * len(nums)
        output = [1] * len(nums)

        leftProducts[0] = 1
        rightProducts[len(nums)-1] = 1

        for i in range(1, len(nums)):
            leftProducts[i] = leftProducts[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):    
            rightProducts[i] = rightProducts[i+1] * nums[i+1]
        for i in range(0, len(nums)):
            output[i] = leftProducts[i] * rightProducts[i]
        return output