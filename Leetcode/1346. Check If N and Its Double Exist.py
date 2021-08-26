class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        buffer = set()
        for x in arr:
            if 2 * x in buffer or (x // 2 in buffer and x % 2 == 0):
                return True
            else:
                buffer.add(x)
        return False
