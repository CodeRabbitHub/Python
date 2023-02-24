def mod_ascii(string: str, cell_number: int) -> int:
    return sum(ord(char) for char in string) % cell_number


print(mod_ascii("ABC", 24))  # prints 6
