class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        if not nums:
            return [-1, -1]

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                a = self.first_less(nums, target, start, mid)
                b = self.last_more(nums, target, mid, end)
                return [a, b]

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return [-1, -1]

    def first_less(self, nums, target, start, end):

        if nums[start] == target:
            return start

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                end = mid - 1
            if nums[mid] < target:
                if nums[mid + 1] == target:
                    return mid + 1
                start = mid + 1

        return -1

    def last_more(self, nums, target, start, end):

        if nums[end] == target:
            return end

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                if nums[mid + 1] > target:
                    return mid
                start = mid + 1
            if nums[mid] > target:
                end = mid - 1

        return -1
