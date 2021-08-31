class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        hashmap = {}
        for idx, num in enumerate(nums):
            if num in hashmap and idx - hashmap[num] <= k:
                return True
            hashmap[num] = idx
        return False
