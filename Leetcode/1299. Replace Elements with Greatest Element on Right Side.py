class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maximum = -1
        for i in range(len(arr) - 1, -1, -1):
            value = arr[i]
            arr[i] = maximum
            if value > maximum:
                maximum = value
        return arr
