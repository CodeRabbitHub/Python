class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(x ** 2 for x in nums)


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        insert_loc = len(nums) - 1

        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                result[insert_loc] = nums[right] ** 2
                insert_loc -= 1
                right -= 1
            else:
                result[insert_loc] = nums[left] ** 2
                insert_loc -= 1
                left += 1
        return result
