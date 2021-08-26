class Solution:
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<= 1
            if n & 1 > 0:
                result += 1
            n >>= 1
        return result
