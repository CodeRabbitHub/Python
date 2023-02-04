# Importing the datetime library
import datetime

# Getting the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# Extracting components of the datetime object
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)

# Formatting the datetime object as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_datetime)


# Importing the time library
import time

# Getting the current time in seconds since the epoch
current_time = time.time()
print("Current time in seconds since the epoch:", current_time)

# Sleeping for 5 seconds
print("Sleeping for 5 seconds...")
time.sleep(5)

# Measuring the elapsed time
start_time = time.time()
print("Doing some time-consuming task...")
time.sleep(2)
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")

import random

# The random module provides functions for generating random numbers
# in a variety of ways.

# random.randint generates a random integer between two given values
# inclusive. For example, the line below generates a random integer between
# 1 and 100:
random_int = random.randint(1, 100)
print("Random integer between 1 and 100:", random_int)

# random.uniform generates a random floating point number between two
# given values. For example, the line below generates a random float between
# 0 and 1:
random_float = random.uniform(0, 1)
print("Random float between 0 and 1:", random_float)

# random.choice can be used to select a random item from a list or
# any other iterable. For example, the line below selects a random fruit
# from a list of fruits:
fruits = ["apple", "banana", "cherry", "durian"]
random_fruit = random.choice(fruits)
print("Random fruit from list:", random_fruit)

# random.shuffle can be used to shuffle items in a list randomly.
# For example, the line below shuffles the list of fruits:
random.shuffle(fruits)
print("Shuffled list of fruits:", fruits)

# random.sample can be used to select a specified number of items
# randomly from a list without replacement. For example, the line below
# selects 3 random fruits from the list:
random_fruits = random.sample(fruits, 3)
print("Random sample of 3 fruits:", random_fruits)
