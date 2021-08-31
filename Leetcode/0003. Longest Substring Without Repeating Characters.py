class Solution:
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        left, right, max_length = 0, 0, 0

        while left < len(s) and right < len(s):
            char = s[right]
            if char in hashmap:
                left = max(left, hashmap[char] + 1)
            hashmap[char] = right
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
