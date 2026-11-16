class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while (left <= right):
            middle = left + (right - left) // 2
            if (nums[middle] == target): 
                return middle
            if (target > nums[middle]): 
                left = middle + 1
            if (target < nums[middle]):
                right = middle - 1

        return -1