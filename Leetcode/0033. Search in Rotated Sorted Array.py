class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # obvious
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                # we are on left side from the point of smallest element
                if target > nums[mid] or target < nums[left]:
                    # search on right side
                    left = mid + 1
                else:
                    # serach on left side
                    right = mid - 1
            else:
                # we are on right side from the point of smallest element
                if target < nums[mid] or target > nums[right]:
                    # search on left side
                    right = mid - 1
                else:
                    # search on right side
                    left = mid + 1
        return -1
