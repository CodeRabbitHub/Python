class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def delete(self, word: str) -> None:
        def _delete(node, word, depth):
            if not node:
                return False

            if depth == len(word):
                if node.end_of_word:
                    node.end_of_word = False
                    return len(node.children) == 0
                return False

            char = word[depth]
            should_delete_current_node = _delete(
                node.children.get(char), word, depth + 1
            )

            if should_delete_current_node:
                node.children.pop(char)
                return len(node.children) == 0

            return False

        _delete(self.root, word, 0)


trie = Trie()
trie.insert("App")
trie.insert("Appl")
trie.delete("App")
print(trie.search("App"))  # prints False
