class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if not (n - 1) in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
