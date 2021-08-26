class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = x + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([x, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
