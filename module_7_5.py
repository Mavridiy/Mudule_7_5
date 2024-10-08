import os
from datetime import datetime

for root, dirs, files in os.walk(r'H:\Program Files\PycharmProjects\pythonProject_new\Homework\Mudule_7_5\folder'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = datetime.fromtimestamp(filetime).strftime("%d.%m.%Y %H:%M")
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь к файлу: {filepath},Размер: {filesize} байт,'
              f'Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
