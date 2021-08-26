class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        length = 0
        zeros_count = 0
        left, right = 0, 0

        while right < len(nums):
            if nums[right] == 0:
                zeros_count += 1

            while zeros_count == 2:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            length = max(length, right - left + 1)
            right += 1
        return length
