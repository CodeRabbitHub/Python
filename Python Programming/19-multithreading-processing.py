# my_thread.py
import threading
import time


def long_running_thread(id):
    print(f"Thread {id} started")
    # Simulate a long running thread
    time.sleep(3)
    print(f"Thread {id} ended")


def run_threads(num_threads):
    print("Multithreading example:")
    threads = []
    for i in range(num_threads):
        # Create a thread and run the long_running_thread function
        thread = threading.Thread(target=long_running_thread, args=(i,))
        threads.append(thread)
        thread.start()
    # Wait for all threads to finish
    for thread in threads:
        thread.join()


# my_process.py
import multiprocessing
import time


def long_running_process(id):
    print(f"Process {id} started")
    # Simulate a long running process
    time.sleep(3)
    print(f"Process {id} ended")


def run_processes(num_processes):
    print("Multiprocessing example:")
    processes = []
    for i in range(num_processes):
        # Create a process and run the long_running_process function
        process = multiprocessing.Process(target=long_running_process, args=(i,))
        processes.append(process)
        process.start()
    # Wait for all processes to finish
    for process in processes:
        process.join()


# main.py
import my_thread
import my_process

my_thread.run_threads(5)
my_process.run_processes(5)
