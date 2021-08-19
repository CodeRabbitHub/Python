# You are a professional robber planning to rob houses along a street. Each house
# has a certain amount of money stashed, the only constraint stopping you from
# robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into
# on the same night.
# Given an integer array nums representing the amount of money of each house, return
# the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        dp = {}
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(nums[i], nums[0])
            else:
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[i]

    def rob2(self, nums: list[int]) -> int:
        prev = curr = 0
        for num in nums:
            temp = prev  # This represents the nums[i-2]th value
            prev = curr  # This represents the nums[i-1]th value
            curr = max(num + temp, prev)  # Here we just plug into the formula
        return curr


nums = [1, 1, 4, 1, 2, 10]

s = Solution()
print(s.rob(nums))
