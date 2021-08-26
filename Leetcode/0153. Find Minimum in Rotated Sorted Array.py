# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become: [4,5,6,7,0,1,2] if it was
# rotated 4 times. Given the sorted rotated array nums of unique elements, return the
# minimum element of this array. You must write an algorithm that runs in O(log n) time.


class Solution:
    def findMin(self, nums: list[int]) -> int:
        result = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            middle = (left + right) // 2
            result = min(result, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1

        return result
