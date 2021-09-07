class TrieNode:
    def __init__(self):
        self.children = {}
        self.amount = 0


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        # To check If the key already exists. If yes, then the original
        # key-value pair will be overwritten to the new one
        self.keys = {}

    def insert(self, key: str, val: int) -> None:

        # compensating the value if the key already exists
        # If not delta will be zero
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val

        CurrNode = self.root
        CurrNode.amount += delta

        for char in key:
            if char not in CurrNode.children:
                CurrNode.children[char] = TrieNode()
            CurrNode = CurrNode.children[char]
            CurrNode.amount += delta

    def sum(self, prefix: str) -> int:

        CurrNode = self.root
        for char in prefix:
            if char not in CurrNode.children:
                return 0
            CurrNode = CurrNode.children[char]

        return CurrNode.amount
