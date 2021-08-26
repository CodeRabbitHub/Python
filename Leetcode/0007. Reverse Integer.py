# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit
# integer range [-2^31, 2^31 - 1], then return 0.


class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0

        if x < -(2 ** 31) or x > (2 ** 31) - 1:
            return 0

        newNumber = 0
        tempNumber = abs(x)

        while tempNumber > 0:
            newNumber = (newNumber * 10) + tempNumber % 10
            tempNumber = tempNumber // 10

        if newNumber < -(2 ** 31) or newNumber > (2 ** 31) - 1:
            return 0

        if x < 0:
            return -1 * newNumber
        else:
            return newNumber


s1 = 123
s2 = -234
s3 = 0
s4 = 1534236469


s = Solution()

print(s.reverse(s1))
print(s.reverse(s2))
print(s.reverse(s3))
print(s.reverse(s4))
