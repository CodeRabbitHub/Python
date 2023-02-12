class BubbleSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort = BubbleSort()
sorted_arr = bubble_sort.sort(arr)
print("Sorted array is:", sorted_arr)
