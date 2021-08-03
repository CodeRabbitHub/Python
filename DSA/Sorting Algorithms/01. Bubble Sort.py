import math


def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - 1 - i):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)


#  Demonstration
for i in range(6):
    print("\n")
    for j in range(6 - i):
        print(f" {j}-{j+1} ", end=",")


print("\n")
bubbleSort([11, 98, 23, 78, 0, 22, 14, 7, 61, 43, 86, 65])
