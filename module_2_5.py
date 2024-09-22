
def get_matrix (n, m, value):
    # определяем переменные цикла i
    i = 0
    matrix = []
    for i in range(n):
        # определяем переменные цикла j
        j = 0
        matrix_row =[]
        for j in range (m):             #
            matrix_row.append(value)    # присваиваем значения промежуточной переменной
        matrix.append(matrix_row)       # присваиваем значения выходной переменной
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)


