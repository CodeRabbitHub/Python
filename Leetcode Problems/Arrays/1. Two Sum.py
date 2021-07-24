def solution(nums, target):
    hashmap = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], idx]
        hashmap[num] = idx


solution([1, 1], 2)
