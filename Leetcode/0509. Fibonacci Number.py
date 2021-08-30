class Solution:
    # Dynamic programming bottom-up approach - fastest
    def fib(self, n: int) -> int:
        dp = {0: 0, 1: 1}
        if n >= 2:
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # Dynamic programming top-down approach - slow
    def fib(self, n: int) -> int:
        dp = {0: 0, 1: 1}
        if n not in dp:
            dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return dp[n]

    # Divide and conquer - recursion - slow
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    # Tail Recursion
    def fib(self, n, a=0, b=1):
        if n == 0:
            return a
        if n == 1:
            return b
        return self.fib(n - 1, b, a + b)

    # Iterative approach
    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        current = 0
        prev1 = 1
        prev2 = 0

        for i in range(2, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
