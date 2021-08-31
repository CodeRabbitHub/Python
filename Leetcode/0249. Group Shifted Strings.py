from collections import defaultdict


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for s in strings:
            key = tuple()
            for i in range(len(s) - 1):
                difference = 26 + ord(s[i + 1]) - ord(s[i])
                key += (difference % 26,)
            hashmap[key].append(s)
        return hashmap.values()
