def merge(customList, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    leftArray = [0] * n1
    rightArray = [0] * n2

    for i in range(0, n1):
        leftArray[i] = customList[left + i]

    for j in range(0, n2):
        rightArray[j] = customList[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if leftArray[i] <= rightArray[j]:
            customList[k] = leftArray[i]
            i += 1
        else:
            customList[k] = rightArray[j]
            j += 1
        k += 1

    while i < n1:
        customList[k] = leftArray[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = rightArray[j]
        j += 1
        k += 1


def mergeSort(customList, left, right):
    if left < right:
        middle = (left + (right - 1)) // 2
        mergeSort(customList, left, middle)
        mergeSort(customList, middle + 1, right)
        merge(customList, left, middle, right)
    return customList


print(mergeSort([34, 82, 11, 9, 14, 95, 37, 59, 73, 0, 73, 26], 0, 11))
