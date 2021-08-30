class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        stack = []
        for token in tokens:
            if token in operations:
                num_2 = stack.pop()
                num_1 = stack.pop()
                function = operations[token]
                stack.append(function(num_1, num_2))
            else:
                stack.append(int(token))
        return stack.pop()
