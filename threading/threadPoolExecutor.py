from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

def task(id):
    print(f'Начинаем задачу {id}...')
    sleep(1)
    return f'Закончили задачу {id}'

start = perf_counter()

with ThreadPoolExecutor() as executor:
    f1 = executor.submit(task, 1)
    f2 = executor.submit(task, 2)

    print(f1.result())
    print(f2.result())    

finish = perf_counter()

print(f"Выполнение заняло {finish-start} секунд.")