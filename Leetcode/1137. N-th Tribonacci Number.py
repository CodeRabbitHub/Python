class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        cache = [0] * (n)
        cache[1], cache[2] = 1, 1

        for idx in range(3, n + 1):
            cache[idx] = cache[idx - 3] + cache[idx - 2] + cache[idx - 1]

        return cache[n]


# Space Optimization: Iterative
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z
