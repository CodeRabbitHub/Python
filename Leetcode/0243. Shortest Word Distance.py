class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        w1i, w2i, min_so_far = -1, -1, float("inf")

        for i, word in enumerate(wordsDict):
            if word == word1:
                w1i = i
            if word == word2:
                w2i = i
            if w1i >= 0 and w2i >= 0:
                min_so_far = min(min_so_far, abs(w2i - w1i))
        return min_so_far
