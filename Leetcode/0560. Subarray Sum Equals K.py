class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        curSum = 0
        prefixSums = {0: 1}

        for num in nums:
            curSum += num
            diff = curSum - k
            count += prefixSums.get(diff, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

        return count
