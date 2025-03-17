import threading
from math import sqrt

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def find_primes(start, end, result, lock):
    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)
    with lock:
        result.extend(primes)

result = []
lock = threading.Lock()
threads = []
start = 1
end = 100000
num_threads = 4
step = (end - start) // num_threads

for i in range(num_threads):
    s = start + i*step
    e = s + step if i != num_threads-1 else end
    t = threading.Thread(target=find_primes, args=(s, e, result, lock))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(sorted(result))