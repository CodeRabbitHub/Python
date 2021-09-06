class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        # for storing the result
        result = []

        for i in range(1, n + 1):
            # both divisible by 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            # only divisible by 3
            elif i % 3 == 0:
                result.append("Fizz")
            # only divisble by 5
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result
