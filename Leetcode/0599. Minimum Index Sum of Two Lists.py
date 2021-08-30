class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        hashmap, result = {}, []

        l1, l2 = set(list1), set(list2)
        common_restaurants = l1.intersection(l2)

        for x in common_restaurants:
            hashmap[x] = list1.index(x) + list2.index(x)

        minimum_value = min(hashmap.values())
        for key, value in hashmap.items():
            if value == minimum_value:
                result.append(key)
        return result
