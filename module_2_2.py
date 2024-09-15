# Ввод целых чисел
first  = input("Введите первое целое число: ")
try:
    int(first)
except:
    print('Это не похоже на целое число, примем первое целое число равным 1'); first=1
second  = input("Введите второе целое число: ")
try:
    int(second)
except:
    print('Это не похоже на целое число, примем второе целое число равным 2'); second=2
third   = input("Введите третье целое число: ")
try:
    int(third )
except:
    print('Это не похоже на целое число, примем третье целое число равным 3'); third =3
# print (first, second, third)
# блок решения поставленной задачи
if first == second and first == third:
    print (3)
elif first == third or first == second or third == second:
    print (2)
else:
    print (0)