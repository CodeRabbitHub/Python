class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            if num not in hashmap:
                hashmap[target - num] = idx
            else:
                return [hashmap[num], idx]
