# Given a non-empty array of integers nums, every element appears
# twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity
# and use only constant extra space.


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


nums = [4, 1, 2, 1, 2]

s = Solution()

print(s.singleNumber(nums))
