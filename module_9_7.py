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
