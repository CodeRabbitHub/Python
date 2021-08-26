class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 != 0:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums

    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
