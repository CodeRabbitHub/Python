# Using no extra space


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        left = 0
        while left < len(arr) - 1:
            right = len(arr) - 1
            if arr[left] == 0:
                while right > left:
                    arr[right] = arr[right - 1]
                    right -= 1
                arr[left + 1] == 0
                left += 2
            else:
                left += 1


# Using extra space
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        duplicate_array = []
        for num in arr:
            if num != 0:
                duplicate_array.append(num)
            else:
                duplicate_array.append(0)
                duplicate_array.append(0)
        for i in range(len(arr)):
            arr[i] = duplicate_array[i]
