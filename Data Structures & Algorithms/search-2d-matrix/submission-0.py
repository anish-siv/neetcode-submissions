class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = [item for sublist in matrix for item in sublist]

        low = 0
        high = len(flattened) - 1

        while low <= high:
            mid = (low + high) // 2
            if flattened[mid] == target:
                return True
            elif flattened[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

        # print(flattened)