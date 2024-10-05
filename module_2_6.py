def deliteli ( n ):
    result = []
    for i in range(2, n+1):
        if n % i == 0:
            result.append(i)
    return result

def pairs(my_list):
    count = 0
    result = []
    while count < len(my_list)/2:
        result.append(count)
        result.append(len(my_list)-count)
    return result

a = input ("Введите число: ")
my_list = deliteli(int(a))
print  (my_list)
for i in my_list:
    c = pairs (i)
    print ( c )
