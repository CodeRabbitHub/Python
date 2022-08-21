import concurrent.futures
import time

start_time = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} seconds..")
    time.sleep(seconds)
    return f"done sleeping..{seconds}"


# with submit method it returns results as it is completed

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = [executor.submit(do_something, sec) for sec in secs]

#     for f in concurrent.futures.as_completed(results):
#         print(f.result())


# with map method it returns results as it were passes

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


finish_time = time.perf_counter()

print(f"Finished in {round(finish_time-start_time, 2)} second(s)")
