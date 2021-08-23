# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in close_open:
                if stack and stack[-1] == close_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
