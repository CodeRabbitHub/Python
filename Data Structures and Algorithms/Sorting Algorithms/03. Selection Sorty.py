"""
Selection-Sort, Time complexity O(n^2) 
Divide the given array into two parts. Sorted and the
Unsorted. Pick the minimum elemnt in unsorted array
and keep adding to the sorted array repeatedly.
"""


def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i + 1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)


selectionSort([11, 98, 23, 78, 0, 22, 14, 7, 61, 43, 86, 65])
