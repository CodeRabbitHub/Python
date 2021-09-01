class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        x = set(nums1)
        y = set(nums2)
        return list(x.intersection(y))


class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(result) and nums1[i] == result[len(result) - 1]):
                    result.append(nums1[i])
                i += 1
                j += 1

        return result
