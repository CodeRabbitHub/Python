class BucketSort:
    def sort(self, arr):
        n = len(arr)
        max_val = max(arr)
        bucket = [0] * (max_val + 1)
        for i in range(n):
            bucket[arr[i]] += 1
        j = 0
        for i in range(max_val + 1):
            for _ in range(bucket[i]):
                arr[j] = i
                j += 1
        return arr


arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucket_sort = BucketSort()
sorted_arr = bucket_sort.sort(arr)
print("Sorted array is:", sorted_arr)
