from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def task(id):
    print(f'Начинаем задачу {id}...')
    sleep(1)
    return f'Завершили задачу {id}'

start = perf_counter()

with ThreadPoolExecutor() as executor:
    results = executor.map(task, [1,2])
    for result in results:
        print(result)

finish = perf_counter()

print(f"Выполнение заняло {finish-start} секунд.")