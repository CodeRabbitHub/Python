class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda i: i[0])
        for i in range(1, len(intervals)):
            iend = intervals[i - 1][1]
            istart = intervals[i][0]
            if istart < iend:
                return False
        return True
