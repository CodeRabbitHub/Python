class QuickSort:
    def sort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.sort(arr, low, pivot - 1)
            self.sort(arr, pivot + 1, high)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort = QuickSort()
sorted_arr = quick_sort.sort(arr, 0, len(arr) - 1)
print("Sorted array is:", sorted_arr)
