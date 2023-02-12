import multiprocessing


def worker(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        # Do some work with the item
        print("Processing item: ", item)
    print("Worker Exiting")


queue = multiprocessing.Queue()
processes = []
for i in range(5):
    p = multiprocessing.Process(target=worker, args=(queue,))
    processes.append(p)
    p.start()

for item in range(10):
    queue.put(item)

for p in processes:
    queue.put(None)

for p in processes:
    p.join()
