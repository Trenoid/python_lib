import threading
from collections import defaultdict


def count_words(lines, result, lock):
    local_count = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        for word in words:
            local_count[word] += 1
    with lock:
        for k, v in local_count.items():
            result[k] += v


def parallel_word_count(filename, num_threads=4):
    with open(filename, 'r') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_threads
    result = defaultdict(int)
    lock = threading.Lock()
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i != num_threads - 1 else len(lines)
        t = threading.Thread(target=count_words,
                             args=(lines[start:end], result, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return dict(result)


# Использование:
print(parallel_word_count("example.txt"))