import multiprocessing as mp
import time
import math

results_a = []
results_b = []
results_c = []
results_d = []


def make_calculation_one(numbers):
    for num in numbers:
        results_a.append(math.sqrt(num ** 3))


def make_calculation_two(numbers):
    for num in numbers:
        results_b.append(math.sqrt(num ** 4))


def make_calculation_three(numbers):
    for num in numbers:
        results_c.append(math.sqrt(num ** 5))


def make_calculation_four(numbers):
    for num in numbers:
        results_d.append(math.sqrt(num ** 6))


if __name__ == "__main__":

    number_list = list(range(10000000))

    p1 = mp.Process(target=make_calculation_one, args=(number_list,))
    p2 = mp.Process(target=make_calculation_two, args=(number_list,))
    p3 = mp.Process(target=make_calculation_three, args=(number_list,))
    p4 = mp.Process(target=make_calculation_four, args=(number_list,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    end = time.time()

    temp_a = results_a
    temp_b = results_b
    temp_c = results_c
    temp_d = results_d

    print(f"Time taken with multi-processing {end-start} seconds")

    start = time.time()
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)
    make_calculation_four(number_list)
    end = time.time()
    print(f"Time taken with single-processing {end-start} seconds")

    print(results_a == temp_a)
    print(results_b == temp_b)
    print(results_c == temp_c)
    print(results_d == temp_d)
