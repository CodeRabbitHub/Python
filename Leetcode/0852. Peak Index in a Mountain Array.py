class Solution(object):
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            if arr[i] > arr[i + 1]:
                return i


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        return arr.index(max(arr))
