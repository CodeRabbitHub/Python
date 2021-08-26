class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted(i[1] for i in intervals)

        result = count = 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            result = max(result, count)
        return result
