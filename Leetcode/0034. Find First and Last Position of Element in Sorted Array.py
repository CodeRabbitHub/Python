class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return self.boundaries(nums, mid)
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]

    def boundaries(self, nums, mid):
        lower_bound, upper_bound = mid, mid
        while lower_bound > 0:
            if nums[lower_bound - 1] == nums[mid]:
                lower_bound -= 1
            else:
                break
        while upper_bound + 1 < len(nums):
            if nums[upper_bound + 1] == nums[mid]:
                upper_bound += 1
            else:
                break
        return [lower_bound, upper_bound]
