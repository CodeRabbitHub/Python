def heapify(customList, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l

    if r < n and customList[r] < customList[smallest]:
        smallest = r

    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)


def heapSort(customList):
    n = len(customList)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i)

    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
