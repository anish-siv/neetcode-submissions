class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid_index = len(nums) // 2
        middle_value = nums[mid_index]

        if target < middle_value:
            for i in range(0, mid_index):
                if nums[i] == target:
                    return i
        elif target > middle_value:
            for i in range(mid_index, len(nums)):
                if nums[i] == target:
                    return i
        else:
            return mid_index
            
        return -1


# How it works:

#     Check the value in the center of the array.
#     If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
#     Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
#     If the value is found, return the target value index. If the target value is not found, return -1.
