class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)

        for idx in range(n - 1, -1, -1):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits
