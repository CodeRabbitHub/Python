class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return [left + 1, right + 1]
