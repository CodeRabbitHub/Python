class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
