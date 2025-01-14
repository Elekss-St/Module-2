import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for _ in range (100):
            sum_increment = randint(50, 500)
            self.balance += sum_increment
            print(f'Пополнение: {sum_increment}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range (100):
            sum_decrement = randint(50, 500)
            print(f'Запрос на {sum_decrement}')
            if sum_decrement <= self.balance:
                self.balance -= sum_decrement
                print(f'Снятие: {sum_decrement}. Баланс: {self.balance}')
            else:
                self.lock.acquire()
                print(f'Запрос отклонён, недостаточно средств')
            # sleep(0.001)


bk = Bank()


# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')