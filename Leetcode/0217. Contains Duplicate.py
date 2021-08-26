class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True
        return False


nums1 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
nums2 = [1, 2, 3, 4]

s = Solution()

print(s.containsDuplicate(nums1))
print(s.containsDuplicate(nums2))
