class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.endOfString = True

    def search(self, word):
        currNode = self.root
        replace = ""
        for char in word:
            if char not in currNode.children:
                return word
            replace += char
            currNode = currNode.children[char]
            if currNode.endOfString == True:
                return replace
        return word


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = Trie()
        wordsList = sentence.split()

        for rootWord in dictionary:
            trie.insert(rootWord)

        processed_wordList = []

        for word in wordsList:
            processed_wordList.append(trie.search(word))

        return " ".join(processed_wordList)
