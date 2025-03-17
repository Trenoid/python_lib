import threading
import math
from queue import Queue


class Calculator:
    def __init__(self):
        self.tasks = Queue()
        self.results = {}
        self.errors = {}

    def add_task(self, func, args, task_id):
        self.tasks.put((func, args, task_id))

    def _worker(self):
        while True:
            try:
                func, args, task_id = self.tasks.get_nowait()
            except:
                return

            try:
                result = func(*args)
                self.results[task_id] = result
            except Exception as e:
                self.errors[task_id] = str(e)
            finally:
                self.tasks.task_done()

    def run(self, num_threads=4):
        threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=self._worker)
            t.start()
            threads.append(t)

        self.tasks.join()
        return self.results, self.errors


# Пример использования:
calc = Calculator()
calc.add_task(math.factorial, (10,), "factorial")
calc.add_task(pow, (2, 10), "power")
calc.add_task(math.sqrt, (-1,), "sqrt_error")

results, errors = calc.run()
print("Результаты:", results)
print("Ошибки:", errors)