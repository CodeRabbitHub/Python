# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.


class Solution:
    def countSubstrings(self, s: str) -> int:
        if s == "":
            return 0
        count = 0
        for idx in range(len(s)):
            left, right = idx, idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            left, right = idx, idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count
