def custom_write(file_name: str, strings: list):
    string_positions:dict = {}
    string_num = 0
    file = open (file_name, 'w', encoding='utf-8')
    for string in strings:
        string_num += 1
        byte_num = file.tell()
        file.write(f'{string}\n')
        string_positions[(string_num, byte_num)] = string
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)