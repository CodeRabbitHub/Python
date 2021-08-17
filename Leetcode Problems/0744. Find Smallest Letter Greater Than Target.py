# Given a characters array letters that is sorted in non-decreasing order
# and a character target, return the smallest character in the array that
# is larger than target.
import bisect


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        idx = bisect.bisect_right(letters, target)
        return letters[0] if idx == len(letters) else letters[idx]
