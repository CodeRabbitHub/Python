class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index
