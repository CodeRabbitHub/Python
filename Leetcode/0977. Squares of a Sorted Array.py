class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(x ** 2 for x in nums)

    def sortedSquares2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
