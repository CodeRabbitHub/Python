import random
import string
import cache


def random_string(lenght):
    s = ""
    for i in range(lenght):
        s = s + random.choice(string.ascii_letters)
    return s


cache.init()

for n in range(1000):
    while True:
        key = random_string(20)
        if cache.contains(key):
            continue
        else:
            break
    value = random_string(20)
    cache.set(key, value)

    print(f"After {n+1} iterations cache has {cache.size()} entries")
