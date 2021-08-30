class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n not in hashset:
            hashset.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return 1 in hashset
