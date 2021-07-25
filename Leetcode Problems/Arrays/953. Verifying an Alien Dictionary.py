class Solution:
    def isAlienSorted(self, words, order):
        hashmap = {}
        for idx, val in enumerate(order):
            hashmap[val] = idx
