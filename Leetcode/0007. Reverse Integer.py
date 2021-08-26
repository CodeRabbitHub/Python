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
