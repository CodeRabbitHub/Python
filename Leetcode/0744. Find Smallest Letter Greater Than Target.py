import bisect


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        idx = bisect.bisect_right(letters, target)
        return letters[0] if idx == len(letters) else letters[idx]
