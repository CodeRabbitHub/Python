from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        count1, count2 = Counter(nums1), Counter(nums2)

        for char in count1:
            if char in count2:
                minimum = min(count1[char], count2[char])
                temp = [char] * minimum
                result.extend(temp)
        return result


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i1 = 0
        i2 = 0
        intersection = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                intersection.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
        return intersection
