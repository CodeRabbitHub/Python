import collections


class Solution:
    def findDiagonalOrder(self, matrix: list[list[int]]) -> list[int]:
        hashmap = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                hashmap[i + j].append(matrix[i][j])
        result = []
        for entry in hashmap.items():
            if entry[0] % 2 == 0:
                result.extend(entry[1][::-1])
            else:
                result.extend(entry[1])
        return result
