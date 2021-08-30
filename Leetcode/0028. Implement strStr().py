class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        elif len(haystack) < len(needle):
            return -1
        else:
            i = 0
            while i + len(needle) <= len(haystack):
                if haystack[i : i + len(needle)] == needle:
                    return i
                i += 1
            return -1


class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
