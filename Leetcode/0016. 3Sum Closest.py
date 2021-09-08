class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # by closest means the dirrence between the sum and target should be minimun
        # lets set the difference intially to a large number then try to minimize it.
        diff = float("inf")

        # lets sort the array to make use of two pointer approach
        nums.sort()

        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]

                # update difference if less than previous one
                if abs(target - sum) < abs(diff):
                    # we are not using absolute diff because we need exact three numbers sum
                    # which are present in list
                    diff = target - sum

                # adjusting the pointers
                if sum < target:
                    lo += 1
                else:
                    hi -= 1

            # if we found exact sum equals to target then break and return
            if diff == 0:
                break

        # target - minimum difference is the closest sum to target
        return target - diff


# Very fast solution
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: list[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current

        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key=lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[: -k + 1]):
            if i > 0 and x == nums[i - 1]:
                continue
            current = self.KSumClosest(nums[i + 1 :], k - 1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest
