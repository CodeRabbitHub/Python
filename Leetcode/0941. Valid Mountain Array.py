class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:

        if len(arr) < 3:
            return False

        i = 0
        N = len(arr)

        # walk up till we find peak or end
        while i + 1 < N and arr[i] < arr[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False

        # walk down from peak till end
        while i + 1 < N and arr[i] > arr[i + 1]:
            i += 1

        return i == N - 1
