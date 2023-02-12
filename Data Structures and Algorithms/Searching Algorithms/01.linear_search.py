class LinearSearch:
    def search(self, arr, target):
        for i, item in enumerate(arr):
            if item == target:
                return i
        return -1


arr = [1, 2, 3, 4, 5]
target = 4
linear_search = LinearSearch()
result = linear_search.search(arr, target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found in the array")
