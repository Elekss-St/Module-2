class House:

    def __init__(self, name, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < self.number_of_floors:
            for i in range (new_floor):
                print (i+1)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance (other, House):
            return  self.number_of_floors == other.number_of_floors
        print ("!!! Идет сравнение объектов не класса 'House'!!!")

    def __lt__(self, other):
        if isinstance (other, House):
            return self.number_of_floors < other.number_of_floors
        print ("!!! Идет сравнение объектов не класса 'House'!!!")

    def __le__(self, other):
        if isinstance (other, House):
            return self.number_of_floors <= other.number_of_floors
        print ("!!! Идет сравнение объектов не класса 'House'!!!")

    def __gt__(self, other):
        if isinstance (other, House):
            return self.number_of_floors > other.number_of_floors
        print ("!!! Идет сравнение объектов не класса 'House'!!!")

    def __ge__(self, other):
        if isinstance (other, House):
            return self.number_of_floors >= other.number_of_floors
        print ("!!! Идет сравнение объектов не класса 'House'!!!")

    def __ne__(self, other):
        if isinstance (other, House):
            return self.number_of_floors != other.number_of_floors
        print ("!!! Идет сравнение объектов не класса 'House'!!!")

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        else:
            print ("!!! Количество этажей должно быть целым числом (int) !!!")
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors - other
        else:
            print("!!! Количество этажей должно быть целым числом (int) !!!")
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            self.number_of_floors = self.number_of_floors * other
        else:
            print ("!!! Количество этажей должно быть целым числом (int) !!!")
        return self

    def __truediv__(self, other):
        if not isinstance(other, int):
           if other != 0:
               self.number_of_floors = self.number_of_floors // other
           else:
               print ("!_!_!_ На ноль делить нельзя _!_!_!")
        else:
            print ("!!! Количество этажей должно быть целым числом (int) !!!")
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__nt(h1 != h2) # __ne__