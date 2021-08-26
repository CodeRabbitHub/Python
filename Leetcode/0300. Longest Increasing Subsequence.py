# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements
# without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence
# of the array [0,3,1,6,2,2,7].


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i + 1):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
