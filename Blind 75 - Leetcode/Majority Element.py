class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
