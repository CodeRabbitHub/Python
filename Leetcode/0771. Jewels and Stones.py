class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {}
        for x in jewels:
            hashmap[x] = 0
        for x in stones:
            if x in hashmap:
                hashmap[x] += 1
        return sum(hashmap.values())


class Solution(object):
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        return sum(s in jewels_set for s in stones)  # generator
