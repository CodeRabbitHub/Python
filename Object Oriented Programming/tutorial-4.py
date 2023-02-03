def trace(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


class Calculator:
    @trace
    def add(self, a, b):
        return a + b

    @trace
    def multiply(self, a, b):
        return a * b


calculator = Calculator()
result = calculator.add(2, 3)
result = calculator.multiply(result, 4)


"""
In this example:

+ trace is a decorator function that takes a function as an argument.
+ wrapper is a nested function that wraps the function passed to trace. It prints a message before and after calling the function, 
  and returns the result of the function.
+ Calculator is a class with two methods, add and multiply, decorated with the trace decorator.
+ calculator = Calculator() creates an instance of the Calculator class.
+ result = calculator.add(2, 3) calls the add method on the calculator instance, which is actually wrapper, and stores the result in result.
+ result = calculator.multiply(result, 4) calls the multiply method on the calculator instance, which is actually wrapper, and stores the result in result.
 The output of this code will be:

    Calling function: add
    add returned: 5
    Calling function: multiply
    multiply returned: 20

This example demonstrates how decorators can be used inside classes to add functionality to class methods, in this case, logging. 
Decorators can be used to add functionality such as authorization, caching, tracing, and more to class methods or functions.

"""
