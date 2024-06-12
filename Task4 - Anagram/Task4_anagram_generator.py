# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task4_anagram_generator.py
@Date:       29.04.2024
@Time:       11:20
@Author:     Mentor
@Software:   PyCharm
"""
# Импортируем библиотеку случайных чисел
import random

# Импортируем библиотеку для работы со строками
import string
from typing import Tuple, Any


# Импортируем

def random_string_func():
    """
    Функция, создающая случайную строку.
    Символы в строке - прописные и ЗАГЛАВНЫЕ буквы, а также цифры.

    Выходное значение:
        случайная строка
    """
    # Задаем длину строки случайным образом. Значения 5 и 12 -просто так удобно
    random_length = random.randint(5, 12)

    random_string = ''.join(random.choices(string.ascii_letters + string.digits,
                                           k=random_length))

    # Возвращаем случайную строку
    return random_string

def anagrama_string_gen(random_string) -> tuple[Any, int | Any]:
    """
    Функция, создающая на основе входной строки 2 новые:
    первая будет являться анаграммой для входной строки,
    вторая точно не будет анаграммой.

    Входное значение:
        random_string: последовательность символов (слово)

    Выходные значения:
        Результат функции - кортеж, где элемент с индексом
        [0] - строка-анаграмма для входного случайного слова
        [1] - строка, которая НЕ является анаграммой для входного случайн слова
    """
    # Задаем зеркальную строку для случайной строки.
    # Это будет анаграмма по определению, так как все символы от исходного слова
    anagrama = random_string[::-1]

    # Задаем значение, которое точно не будет анаграммой.
    # Умножаем первый символ случайного слова на длину слова - 1
    not_anagrama = random_string[0] * (len(random_string) - 1)

    # Результат функции - кортеж, где [0] элемент - анаграмма, а [1] - нет
    return anagrama, not_anagrama

# Проверка работы описанных функций на определение палиндрома
if __name__ == '__main__':
    # Создаем случайную строку
    example_random_string = random_string_func()
    print('Случайная строка:', example_random_string)
    # При помощи функции генератора анаграммы по исходной строке
    print('Анаграмма       :', anagrama_string_gen(example_random_string)[0])
    print('НЕ анаграмма    :', anagrama_string_gen(example_random_string)[1])

