'''
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое",
если результат 1ой функции будет простым числом и "Составное" в противном случае.
'''

def is_prime(func):
    def wrapper (*args, **kwargs):
        result = func(*args, **kwargs)
        for j in range(2, int(result / 2) + 1):    # перебор делителей от 2 до половины  значения текущего элемента
            if result % j == 0:                    # если делитель есть
                print ('Составное')
                break                               # если есть хоть один делитель прерываем перебор
        else:                                       # иначе пишем в массив простых
            if result != 1:                         # исключаем 1 из простых
                print ('Простое')
    return wrapper

@is_prime
def sum_three(x:int ,y:int,z:int):
    return x+y+z

result = sum_three(2, 3, 6)
print(result)