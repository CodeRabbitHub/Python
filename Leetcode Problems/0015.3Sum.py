# Given an integer array nums, return all the triplets [nums[i],
# nums[j], nums[k]] such that i != j, i != k, and j != k, and
# nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         result = []
#         i = 0
#         while nums[i] < 0:
#             temp = self.twosum(nums[i+1:], - i)
#             if temp:
#                 temp.extend(i)
#                 result.append(temp)
#             i += 1
#         return result


def twoSum(nums, target):
    dix = set()
    for num in nums:
        complement = target - num
        if complement in dix:
            return [complement, num]
        dix.add(num)


print(twoSum([2, 3, 4, 5], 56))
