# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct
# ways can you climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n in [1, 2]:
            return n
        elif n > 2:
            dp[1], dp[2] = 1, 2
            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


s = Solution()

print(s.climbStairs(0))
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(5))
