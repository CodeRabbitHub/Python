# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by
# starti. You are also given an interval newInterval = [start, end] that represents the start and
# end of another interval. Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping intervals (merge
# overlapping intervals if necessary). Return intervals after the insertion.


class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        result.append(newInterval)

        return result
