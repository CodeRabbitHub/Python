# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0:
            return x == self.reverse(x)

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        newNumber = 0
        tempNumber = x

        while tempNumber > 0:
            newNumber = (newNumber * 10) + tempNumber % 10
            tempNumber = tempNumber // 10

        return newNumber


s1 = 121
s2 = -121
s3 = 10
s4 = 0

s = Solution()

print(s.isPalindrome(s1))
print(s.isPalindrome(s2))
print(s.isPalindrome(s3))
print(s.isPalindrome(s4))
