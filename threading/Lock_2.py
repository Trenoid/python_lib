from threading import Thread, Lock
from time import sleep


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def increase(self, by):
        self.lock.acquire()

        current_value = self.value
        current_value += by

        sleep(0.1)

        self.value = current_value
        print(f'Значение counter: {self.value}')

        self.lock.release()


counter = Counter()

# создаем потоки
t1 = Thread(target=counter.increase, args=(10, ))
t2 = Thread(target=counter.increase, args=(20, ))

# запускаем потоки
t1.start()
t2.start()


# ждем завершения потоков
t1.join()
t2.join()


print(f'Значение counter в итоге: {counter.value}')