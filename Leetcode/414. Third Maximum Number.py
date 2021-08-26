class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        firstMax, secondMax, thirdMax = float("-inf"), float("-inf"), float("-inf")

        for i in range(len(nums)):
            if nums[i] > firstMax:
                firstMax, secondMax, thirdMax = nums[i], firstMax, secondMax
            if firstMax > nums[i] > secondMax:
                secondMax, thirdMax = nums[i], secondMax
            if secondMax > nums[i] > thirdMax:
                thirdMax = nums[i]

        return firstMax if thirdMax == float("-inf") else thirdMax
