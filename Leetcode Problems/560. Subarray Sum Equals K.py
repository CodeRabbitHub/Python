class Solution:
    def subbarraySum(nums, k):
        count = 1
        i = 0
        j = i + 1
        while j < len(nums):
            curr_sum = nums[i] + nums[j]
            if curr_sum < k:
                j += 1
            elif curr_sum > k:
                i += 1
            else:
                count += 1
                i += 1
        return count
