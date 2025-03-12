import random
import time
import sys

def print_slow(text):
    for char in text:
        sys.stdout.write(char)  # Выводим букву без перехода на новую строку
        sys.stdout.flush()  # Принудительно обновляем буфер вывода
        time.sleep(0.01)  # Задержка между буквами
    print()  # Перевод строки после завершения вывода


'''def replace_a_with_b(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().replace('а', 'б')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

replace_a_with_b("example.txt")
'''