# Given an integer array nums, find a contiguous non-empty subarray within
# the array that has the largest product, and return the product.


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            curMax, curMin = max(n * curMax, n * curMin, n), min(
                n * curMax, n * curMin, n
            )
            res = max(res, curMax)
        return res
