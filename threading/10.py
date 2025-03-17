import threading
import time
import random


class ParkingLot:
    def __init__(self, capacity):
        self.semaphore = threading.Semaphore(capacity)
        self.capacity = capacity

    def enter(self, car_id):
        if self.semaphore.acquire(blocking=False):
            print(f"Автомобиль {car_id} припарковался. Свободно мест: {self.semaphore._value}")
            return True
        else:
            print(f"Автомобиль {car_id} не нашел места. Уезжает.")
            return False

    def exit(self, car_id):
        self.semaphore.release()
        print(f"Автомобиль {car_id} уехал. Свободно мест: {self.semaphore._value}")


def car_simulation(parking, car_id):
    if parking.enter(car_id):
        time.sleep(random.randint(1, 5))
        parking.exit(car_id)


parking = ParkingLot(3)
cars = [threading.Thread(target=car_simulation, args=(parking, i)) for i in range(10)]

for car in cars:
    car.start()
    time.sleep(random.random())

for car in cars:
    car.join()