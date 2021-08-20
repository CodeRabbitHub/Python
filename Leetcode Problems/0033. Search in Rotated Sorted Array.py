# Given the array nums after the rotation and an integer target, return the
# index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
