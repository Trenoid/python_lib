import threading
from queue import Queue


def worker(task_queue, result_queue):
    while True:
        func, args = task_queue.get()
        if func is None: break
        result = func(*args)
        result_queue.put(result)
        task_queue.task_done()


def parallel_compute(tasks, num_threads=4):
    task_queue = Queue()
    result_queue = Queue()

    for task in tasks:
        task_queue.put(task)

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(task_queue, result_queue))
        t.start()
        threads.append(t)
        task_queue.put((None, None))  # Сигнал завершения

    results = []


    for t in threads:
        t.join()

    for _ in range(len(tasks)):
        results.append(result_queue.get())

    return results


# Пример использования:
tasks = [
    (lambda x: x ** 34, (435,)),
    (lambda x: x ** 3, (3,)),
    (lambda x: x * 2, (10,))
]
print(parallel_compute(tasks, 2))