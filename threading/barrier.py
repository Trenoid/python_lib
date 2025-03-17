#barrier_tut.py
from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num = 4
# 4 threads will need to pass this barrier to get released.
b = Barrier(num)
names = ['Alpha', 'Beta', 'Gamma', 'Delta']

def player():
    name = names.pop()
    sleep(randrange(2, 5))
    print('%s reached the barrier at: %s' % (name, ctime()))
    b.wait()
    
threads = []
print('Race starts now…')

for i in range(num):
    threads.append(Thread(target=player))
    threads[-1].start()
"""
Following loop enables waiting for the threads to complete before moving on with the main script.
"""
for thread in threads:
    thread.join()
print()
print('Race over!')