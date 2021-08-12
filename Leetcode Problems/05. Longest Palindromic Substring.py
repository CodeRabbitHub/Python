# Given a string s, return the longest palindromic substring in s.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    result = s[left : right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    result = s[left : right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1
        return result


s1 = "babad"
s2 = "cbbd"
s3 = "a"
s4 = "ac"

s = Solution()

print(s.longestPalindrome(s1), end="\n")
print(s.longestPalindrome(s2), end="\n")
print(s.longestPalindrome(s3), end="\n")
print(s.longestPalindrome(s4), end="\n")
