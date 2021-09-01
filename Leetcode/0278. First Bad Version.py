# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                # if mid is bad then move the right pointer to mid, mid-1 can be good.
                right = mid
            else:
                # if mid is good then move the left point to mid+1 which can be good or bad.
                left = mid + 1
        return right
