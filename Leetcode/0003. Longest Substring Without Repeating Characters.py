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
