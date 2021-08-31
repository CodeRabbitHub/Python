class TwoSum:
    def __init__(self):
        self.numbers = list()

    def add(self, number: int) -> None:
        self.numbers.append(number)

    def find(self, value: int) -> bool:
        hashset = set()
        for x in self.numbers:
            if x not in hashset:
                hashset.add(value - x)
            else:
                return True
        return False
