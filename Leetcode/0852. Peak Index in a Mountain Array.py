class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        return arr.index(max(arr))
