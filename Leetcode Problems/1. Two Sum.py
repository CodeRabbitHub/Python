# Given an array of integers nums and an integer target, return
# indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.


def solution(nums, target):
    hashmap = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], idx]
        hashmap[num] = idx


nums = [3, 9, 5, 1, 6, 11, 4]
target = 17

print(solution(nums, target))
