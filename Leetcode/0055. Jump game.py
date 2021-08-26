class Solution:
    def canJump(self, nums: list[int]) -> bool:
        end = len(nums) - 1

        for idx in range(len(nums) - 1, -1, -1):
            if idx + nums[idx] >= end:
                end = idx
        return True if end == 0 else False
