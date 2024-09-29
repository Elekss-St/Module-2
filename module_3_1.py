# определение глобального счетчика
calls = 0
# Функция подсчета вызовов
def count_calls():
    global calls
    calls = calls + 1
    return
# функция string_info
def string_info(string_input):
    # вызов функции count_calls
    count_calls()
    tuple_len_string_input = (len(string_input))
    string_input_upper = (string_input.upper())
    string_input_lower = (string_input.lower())
    return tuple_len_string_input, string_input_upper, string_input_lower
# функция is_contains
def is_contains(string_input, var_list):
    # вызов функции count_calls
    count_calls()
    result = False
    # начало цикла
    for i in range (len(var_list)):
        if var_list[i].lower() == string_input.lower():
            result = True
            break
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
