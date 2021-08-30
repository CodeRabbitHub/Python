class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = [word[::-1] for word in s]
        return " ".join(s)
