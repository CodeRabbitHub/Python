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
