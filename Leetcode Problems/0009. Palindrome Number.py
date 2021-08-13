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
