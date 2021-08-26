class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True
        return False
