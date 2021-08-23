# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1.


class Solution:
    # Dynamic programming bottom-up approach
    def fib(self, n: int) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 1
        if n > 1:
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # Dynamic programming top-down approach
    def fib2(self, n: int, dp={}) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n not in dp:
            dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return dp[n]

    # Divide and conquer - recursion
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)
