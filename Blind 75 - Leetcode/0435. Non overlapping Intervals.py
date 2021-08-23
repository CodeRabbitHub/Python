class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        left, right = 0, 1
        count = 0

        while right < n:
            if intervals[left][1] <= intervals[right][0]:
                left = right
                right += 1
            elif intervals[left][1] <= intervals[right][1]:
                count += 1
                right += 1
            elif intervals[left][1] > intervals[right][1]:
                count += 1
                left = right
                right += 1
        return count
