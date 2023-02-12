class InsertionSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort = InsertionSort()
sorted_arr = insertion_sort.sort(arr)
print("Sorted array is:", sorted_arr)
