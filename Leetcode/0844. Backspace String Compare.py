import itertools


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.finalWord(s) == self.finalWord(t)

    def finalWord(self, nums):
        word = []
        for i in nums:
            if i != "#":
                word.append(i)
            elif word:
                word.pop()
        return "".join(word)


class Solution:
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
