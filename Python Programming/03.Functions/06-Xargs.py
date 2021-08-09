def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(multiply(2, 3, 4, 5))
