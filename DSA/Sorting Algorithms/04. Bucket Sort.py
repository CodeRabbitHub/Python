from InsertionSort import insertionSort
import math


def bucketSort(customList):
    numBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    # Creating buckets
    for i in range(numBuckets):
        arr.append([])

    # Shifting elemets to buckets
    for j in range(customList):
        index_b = math.ceil(j * numBuckets / maxValue)
        arr[index_b - 1].append(j)

    # Sorting the elements in bucket
    for i in range(numBuckets):
        arr[i] = insertionSort(arr[i])

    # Finally bring the elements form bucket into the list
    k = 0
    for i in range(numBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1

    print(customList)

    bucketSort([11, 98, 23, 78, 0, 22, 14, 7, 61, 43, 86, 65])
