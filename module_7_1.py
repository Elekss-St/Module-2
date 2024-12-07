from pprint import pprint

class Product():

    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        result = file.read()
        file.close()
        return result
# В текущем варианте будет вывод как указано в задании
    def  add(self, *products):
        for i in products:
            if str(i) in self.get_products():
                print (f'Продукт {i} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()

# Если использовать такой вариант, то это будет соответствовать тексту ТЗ
# где написано "Добавляет в файл __file_name каждый продукт из products,
# если его ещё нет в файле (по названию)".
# Но при этом вывод не будет соответствовать ТЗ
#
#    def  add(self, *products):
#        for i in products:
#            if str(i.name) in self.get_products():
#                print (f'Продукт {i.name} уже есть в магазине')
#            else:
#                file = open(self.__file_name, 'a')
#                file.write(f'{i}\n')
#                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
