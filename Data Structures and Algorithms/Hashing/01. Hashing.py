def mod(number, cellNumber):
    return number % cellNumber


def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber


print(modASCII("ABC", 24))
