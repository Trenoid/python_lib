import threading
from math import prod


def factorial(start, end, result):
    res = prod(range(start, end + 1))
    print(res)
    result.append(res)


def parallel_factorial(n, num_threads=4):
    step = n // num_threads
    result = []
    threads = []

    for i in range(num_threads):
        s = 1 + i*step
        e = (i + 1) * step if i != num_threads - 1 else n
        t = threading.Thread(target=factorial, args=(s, e, result))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return prod(result)


print(parallel_factorial(6))