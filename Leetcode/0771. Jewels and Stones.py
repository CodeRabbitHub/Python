class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {}
        for x in jewels:
            hashmap[x] = 0
        for x in stones:
            if x in hashmap:
                hashmap[x] += 1
        return sum(hashmap.values())
