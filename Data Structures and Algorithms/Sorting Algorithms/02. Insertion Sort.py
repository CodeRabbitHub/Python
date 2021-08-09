"""
Insertion Sort, Tiime complexity
Divide the given array into two parts. Then take
first element from unsorted array and find its
correct position in sorted array. Repeat until
unsorted array is empty.
"""


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    print(customList)


insertionSort([11, 98, 23, 78, 0, 22, 14, 7, 61, 43, 86, 65])
