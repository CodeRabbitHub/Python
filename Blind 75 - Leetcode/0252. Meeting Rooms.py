# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda i: i[0])
        for i in range(1, len(intervals)):
            iend = intervals[i - 1][1]
            istart = intervals[i][0]
            if istart < iend:
                return False
        return True


intervals1 = [[0, 30], [5, 10], [15, 20]]
intervals2 = [[7, 10], [2, 4]]

s = Solution()

print(s.canAttendMeetings(intervals1))
print(s.canAttendMeetings(intervals2))
