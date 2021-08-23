# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
# and return its sum.


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub


nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
nums3 = [5, 4, -1, 7, 8]

s = Solution()

print(s.maxSubArray(nums1))
print(s.maxSubArray(nums2))
print(s.maxSubArray(nums3))
