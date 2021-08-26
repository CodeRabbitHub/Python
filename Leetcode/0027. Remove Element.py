class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left

    def removeElement2(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
            index += 1
        return index
