'''
Задача:
Напишите функцию-генератор all_variants(text),
которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
'''

def all_variants(text):
    for _i in range(len(text)):
        for _j in range(len(text) - _i):
            yield text[_j:_j + 1 + _i]



a = all_variants("abc")
for i in a:
    print(i)
