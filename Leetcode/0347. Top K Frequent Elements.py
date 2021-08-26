# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            frequency[c].append(n)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        return [x for x, y in collections.Counter(nums).most_common(k)]
