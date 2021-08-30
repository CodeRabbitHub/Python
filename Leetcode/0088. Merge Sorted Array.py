class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
