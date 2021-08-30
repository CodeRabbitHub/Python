class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        sorted_nums = sorted(nums)
        if sorted_nums[-1] >= 2 * sorted_nums[-2]:
            return nums.index(sorted_nums[-1])
        return -1


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        index = -1
        largest = float("-inf")
        second = float("-inf")
        for idx, num in enumerate(nums):
            if num > largest:
                second = largest
                largest = num
                index = idx
            elif num > second:
                second = num
        if largest >= second * 2:
            return index
        else:
            return -1
