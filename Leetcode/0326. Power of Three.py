class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # if number is less than zero
        if n <= 0:
            return False

        # keep dividing the number by three and update the number
        # until its no more divisble by 3
        while n % 3 == 0:
            n /= 3

        # check if quotient is one then return true
        return n == 1
