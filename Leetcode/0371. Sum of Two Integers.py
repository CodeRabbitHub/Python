class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)

        # ensuring X is bigger than y
        if x < y:
            return self.getSum(b, a)

        # retaining the sign
        sign = 1 if a > 0 else -1

        # addition of two positive numbers
        if a * b >= 0:
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:  # addition of one positive and one negative number
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow
        return x * sign
