# Given an array of integers nums and an integer target, return
# indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], idx]
            hashmap[num] = idx


nums1, target1 = [2, 7, 11, 15], 9
nums2, target2 = [3, 2, 4], 6
nums3, target3 = [3, 3], 6

s = Solution()

print(s.twoSum(nums1, target1), end="\n")
print(s.twoSum(nums2, target2), end="\n")
print(s.twoSum(nums3, target3), end="\n")
