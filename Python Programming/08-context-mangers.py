# Introduction to Context Managers in Python

# Context managers are used to manage resources such as files, sockets, and database connections. They allow you to ensure that resources are
# properly acquired and released, even in the presence of exceptions.

# The with Statement
# The with statement is used to wrap the execution of a block of code with methods defined by a context manager.
# The with statement ensures that the resources are properly acquired and released, even if an exception occurs.

# Example: Using the with statement to open a file
with open("file.txt") as file:
    # Code that operates on the file
    data = file.read()

# The contextmanager Decorator
# The contextmanager decorator can be used to turn a generator function into a context manager.
# The generator should yield exactly once and should use the yield statement to specify the resource being managed.

# Example: Implementing a context manager using the contextmanager decorator
from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()


# Use the context manager
with open_file("file.txt", "r") as file:
    # Code that operates on the file
    data = file.read()

# Context Managers and Databases
# Context managers can be used to manage database connections, ensuring that connections are properly acquired and released.

# Example: Implementing a context manager to manage a database connection
import psycopg2


@contextmanager
def open_db_connection():
    conn = psycopg2.connect("dbname=test user=postgres password=secret")
    try:
        yield conn
    finally:
        conn.close()


# Use the context manager
with open_db_connection() as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM table")
    rows = cur.fetchall()

# Context Managers and Locks
# Context managers can be used to manage locks, ensuring that locks are properly acquired and released.

# Example: Implementing a context manager to manage a lock
import threading


@contextmanager
def lock(lock):
    lock.acquire()
    try:
        yield
    finally:
        lock.release()


# Use the context manager
lock = threading.Lock()
with lock:
    # Code that requires the lock
    print("Code inside the with block is executed atomically")

# Conclusion
# Context managers are a powerful tool for managing resources such as files, sockets, and database connections.
# They allow you to ensure that resources are properly acquired and released, even in the presence of exceptions.
# The with statement, the contextmanager decorator, and custom context managers can be used to implement context managers in Python.
