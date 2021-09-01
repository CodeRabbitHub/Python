class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # check if we already at peak
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                # we are on upward left slope and the peak must be on right
                left = mid + 1
            else:
                # we are on downward right slope and the peak must be on left
                right = mid - 1

        return left
