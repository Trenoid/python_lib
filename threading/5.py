from threading import Thread
import random

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def threaded_sort(arr, num_threads=4):
    if len(arr) <= 1:
        return arr

    chunks = []
    chunk_size = len(arr) // num_threads
    threads = []

    for i in range(num_threads):
        start = i*chunk_size
        end = start + chunk_size if i != num_threads-1 else len(arr)
        chunk = arr[start:end]
        t = Thread(target = lambda c: c.sort(),args=(chunk,))
        threads.append(t)
        t.start()

        chunks.append(chunk)

    for t in threads:
        t.join()

    while len(chunks) > 1:
        new_chunks = []
        for i in range(0, len(chunks), 2):
            if i + 1 < len(chunks):
                new_chunks.append(merge(chunks[i], chunks[i + 1]))
            else:
                new_chunks.append(chunks[i])
        chunks = new_chunks

    return chunks[0]


arr = [random.randint(0, 1000) for _ in range(100000)]