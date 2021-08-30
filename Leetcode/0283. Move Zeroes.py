class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = j = 0
        N = len(nums)
        while j < N:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        for idx in range(i, N):
            nums[idx] = 0
        return nums


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == 0:
                i = left
                while i < right:
                    nums[i] = nums[i + 1]
                    i += 1
                nums[right] = 0
                right -= 1
            else:
                left += 1
        return nums
