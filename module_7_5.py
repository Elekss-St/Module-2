import os
import time
from os.path import join, getmtime, getsize, dirname

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = join(root, file)
        filetime = getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = getsize(filepath)
        parent_dir = dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
