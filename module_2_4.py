# Решение 1 вариант
# Получаем входные двнные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# определяем выходные массивы и переменную is_prime
primes = []
not_primes = []
for i in range(0, len(numbers)):            # Перебор входного массива значений
    k = 0                                   # устанавливаем счетчик делителей
    for j in range(2, int(numbers[i]/2)+1): # перебор делителей от 2 до половины  значения текущего элемента
        if numbers[i] % j == 0:             # если делитель есть увеличиваем счетчик на 1
            k = k + 1
    if k == 0:                              # по окончании перебора проверяем наличие целочисленных делителей
        if numbers[i] != 1:                 # исключаем 1 из простых
            primes.append(numbers[i])       # пишем в массив простых
    else:
        not_primes.append(numbers[i])       # иначе пишем в массив составных
# по окончании цикла печатаем получившиеся переменные
print ("Primes :", primes, "\nNot primes :", not_primes)

# Решение 2 вариант
print ('\nНемного улучшенное решение , с прерыванием после нахождения  первого делителя \n')
# Получаем входные двнные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# определяем выходные массивы
primes = []
not_primes = []
for i in range(0, len(numbers)):            # Перебор входного массива значений
    for j in range(2, int(numbers[i]/2)+1): # перебор делителей от 2 до половины  значения текущего элемента
        if numbers[i] % j == 0:             # если делитель есть
            not_primes.append(numbers[i])   # то пишем в массив не простых чисел
            break                           # если есть хоть один делитель прерываем перебор
    else:                                   # иначе пишем в массив простых
        if numbers[i] != 1:                 # исключаем 1 из простых
            primes.append(numbers[i])
# по окончании цикла печатаем получившиеся переменные
print ("Primes :", primes, "\nNot primes :", not_primes)



