class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i + 1):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
