class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        left = 0
        while left < len(arr) - 1:
            right = len(arr) - 1
            if arr[left] == 0:
                while right > left:
                    arr[right] = arr[right - 1]
                    right = right - 1
                arr[left + 1] == 0
                left = left + 2
            else:
                left += 1
