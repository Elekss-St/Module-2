# Подсчет суммы длинн элементов и значений чисел. Имеющиеся проверки касаются
# только следующих типов  INT , STR , LIST , SET , TUPLE , DICT. Правил преобразования
# для типов FLOAT , COMPLEX  в задании не указано. Функция перебирает все элементы входного массива ,
# если элементы могут быть подсчитаны в текущей итерации - они считаются ,
# иначе рекурсивно вызывается функция с приведением текущего элемента к подсчитываемому виду.
arg_sum = 0

def calculate_structure_sum(args):
    global arg_sum
    for i in range(len(args)):
        if isinstance(args[i],(int)):
            arg_sum = arg_sum + args[i]
        if isinstance(args[i], (str)):
            arg_sum = arg_sum + len(args[i])
        if isinstance(args[i], (list)):
            res = calculate_structure_sum(args[i])
        if isinstance(args[i], (tuple)):
            res = calculate_structure_sum(list(args[i]))
        if isinstance(args[i], (set)):
            res = calculate_structure_sum(list(args[i]))
        if isinstance(args[i], (dict)):
            res = calculate_structure_sum(list(args[i].items()))
    return arg_sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)