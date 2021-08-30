class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            num_of_digits = 0
            while num:
                num = num // 10
                num_of_digits += 1
            if num_of_digits % 2 == 0:
                count += 1
        return count
