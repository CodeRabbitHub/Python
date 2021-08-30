class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        x = set(nums1)
        y = set(nums2)
        return list(x.intersection(y))
