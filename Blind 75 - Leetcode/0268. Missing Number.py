# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

s = Solution()

print(s.missingNumber(nums))
