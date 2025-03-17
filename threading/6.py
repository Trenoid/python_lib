import threading
import time


class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance  # Начальный баланс счета
        self.lock = threading.Lock()  # Блокировка для синхронизации
        self.condition = threading.Condition(self.lock)  # Условие для ожидания

    def withdraw(self, amount, customer_name):
        with self.condition:  # Автоматически захватывает блокировку
            while self.balance < amount:  # Пока недостаточно средств
                print(f"{customer_name} ждет. Требуется: {amount}, Доступно: {self.balance}")
                self.condition.wait()  # Ожидание уведомления

            # Снятие денег
            self.balance -= amount
            print(f"{customer_name} снял {amount}. Остаток: {self.balance}")
            self.condition.notify_all()  # Уведомление всех ожидающих потоков


def customer_task(account, amount, name):
    print(f"{name} пытается снять {amount}")
    account.withdraw(amount, name)


# Создание счета с начальным балансом 1500
account = BankAccount(1600)

# Создание клиентов (потоков) с разными суммами для снятия
customers = [
    threading.Thread(target=customer_task, args=(account, 800, "Клиент-1")),
    threading.Thread(target=customer_task, args=(account, 500, "Клиент-2")),
    threading.Thread(target=customer_task, args=(account, 400, "Клиент-3")),
    threading.Thread(target=customer_task, args=(account, 300, "Клиент-4"))
]

# Запуск всех потоков
for c in customers:
    c.start()
    time.sleep(0.1)  # Имитация задержки между операциями

# Ожидание завершения всех потоков
for c in customers:
    c.join()

print(f"Итоговый баланс: {account.balance}")