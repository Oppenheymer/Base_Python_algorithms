# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task5_vowels_generator.py
@Date:       12.06.2024
@Time:       14:51
@Author:     Mentor
@Software:   PyCharm
"""
# Импортируем библиотеку случайных чисел
import random

# Импортируем библиотеку для работы со строками
import string

def random_string_func():
    """
    Функция, создающая случайную строку.
    Символы в строке - прописные и ЗАГЛАВНЫЕ буквы, а также цифры.

    Выходное значение:
        случайная строка
    """
    # Задаем длину строки случайным образом. Значения 5 и 12 -просто так удобно
    random_length = random.randint(5, 12)

    random_string = ''.join(random.choices(string.ascii_letters,
                                        k=random_length))

    # Возвращаем случайную строку
    return random_string


# Проверка работы описанных функций на создание случайной строки
if __name__ == '__main__':
    # Создаем случайную строку
    example_random_string = random_string_func()
    print('Случайная строка:', example_random_string)
