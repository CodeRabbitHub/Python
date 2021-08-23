# Given a string s, find the length of the longest
# substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        left = 0
        right = 0
        max_len = 0

        while left < len(s) and right < len(s):
            char = s[right]
            if char in hashmap:
                left = max(left, hashmap[char] + 1)
            hashmap[char] = right
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = ""

s = Solution()

print(s.lengthOfLongestSubstring(s1), end="\n")
print(s.lengthOfLongestSubstring(s2), end="\n")
print(s.lengthOfLongestSubstring(s3), end="\n")
print(s.lengthOfLongestSubstring(s4), end="\n")
