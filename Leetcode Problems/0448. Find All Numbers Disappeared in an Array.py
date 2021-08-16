# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []
        s = set(nums)

        for num in range(1, len(nums) + 1):
            if num not in s:
                result.append(num)
        return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]

s = Solution()

print(s.findDisappearedNumbers(nums))
