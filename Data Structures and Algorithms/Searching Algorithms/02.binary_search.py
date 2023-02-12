class BinarySearch:
    def search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


arr = [1, 2, 3, 4, 5]
target = 4
binary_search = BinarySearch()
result = binary_search.search(arr, target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found in the array")
