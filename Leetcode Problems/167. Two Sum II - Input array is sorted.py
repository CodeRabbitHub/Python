# Given an array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up
# to a specific target number.


class Solution:
    def twosumII(self, nums, target):

        i, j = 0, len(nums) - 1

        while i < j:
            curr_sum = nums[i] + nums[j]
            if curr_sum > target:
                j -= 1
            elif curr_sum < target:
                i += 1
            else:
                return [i + 1, j + 1]


sol = Solution()
print(sol.twosumII([2, 7, 11, 15], 9))
