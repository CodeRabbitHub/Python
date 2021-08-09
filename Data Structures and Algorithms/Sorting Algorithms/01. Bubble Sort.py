"""
Bubble - Sort, Time complexity O(n^2) 
We compare each pair of adjacent items and swap them
if they are in wrong order.

Explanation: Say there are 7 (n) objects in our list
[0,1,2,3,4,5,6] Then number of iterations needed for 
comparing the objects to find largest calue is 6 (n-1).
For each iterations (i). We are fixing the largest number
at end of our list. So we are iterating one element less
for each iteration (i-1).
"""

# Demonstration

for i in range(6):
    print("\n")
    for j in range(6 - i):
        print(f" {j}-{j+1} ", end=",")
    print({j + 1})

# Bubble sort function


def bubbleSort(customList):
    num_of_iterations = len(customList) - 1
    for i in range(num_of_iterations):
        for j in range(num_of_iterations - i):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)


print("\n")
bubbleSort([11, 98, 23, 78, 0, 22, 14, 7, 61, 43, 86, 65])
