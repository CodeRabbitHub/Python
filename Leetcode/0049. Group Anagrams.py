from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            hashmap[tuple(sorted(word))].append(word)
        return hashmap.values()
