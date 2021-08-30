from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution:
    def isAnagram(self, s, t):
        if len(s) == len(t):
            return sorted(s) == sorted(t)
        return False
