# Write a function to find the longest common prefix string
# amongst an array of strings. If there is no common prefix,
# return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs, key=len)
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            first_word = strs[0]
            pos = 0
            for char in first_word:
                if self.pos_char(strs, pos, char):
                    pos += 1
                else:
                    break
            return first_word[:pos]

    def pos_char(self, strs, pos, char):
        for string in strs:
            if char not in string[pos]:
                return False
        return True


s1 = ["flower", "flow", "flight"]
s2 = ["dog", "racecar", "car"]

s = Solution()

print(s.longestCommonPrefix(s1))
print(s.longestCommonPrefix(s2))
