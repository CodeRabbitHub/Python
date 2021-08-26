class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        for i in range(n + 1):
            res.append(bin(i).count("1"))
        return res

    def countBits2(self, n: int) -> list[int]:
        res = [0] * (n + 1)
        for x in range(1, n + 1):
            res[x] = res[x & (x - 1)] + 1
        return res
