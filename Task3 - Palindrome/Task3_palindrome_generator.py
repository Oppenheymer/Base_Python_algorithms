# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task3_palindrome_generator.py
@Date:       20.04.2024
@Time:       12:53
@Author:     Mentor
@Software:   PyCharm
"""

# Импортируем библиотеку случайных чисел
import random
# Импортируем библиотеку для работы со строками
import string

# Импортируем метод проверки на палиндром
from Task3_palindrome import Palindrome


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


def palindrome_string_func():
    """
    Функция, создающая случайную строку, которая будет являться палиндромом.
    Символы в строке - прописные и ЗАГЛАВНЫЕ буквы, а также цифры.

    Выходное значение:
        случайная строка-палиндром
    """
    # В переменную word записываем результат функции, создающей случайн. строку
    random_palindrome_string = random_string_func()

    # Пока мы не получили необходимую строку,
    # используем 1 метод проверки на палиндром
    while Palindrome.mirror_index(
            Palindrome(random_palindrome_string)) != True:
        random_palindrome_string = random_string_func()

    # Возвращаем случайную строку-палиндром
    return random_palindrome_string


# Выполнение тела программы
if __name__ == '__main__':
    # Пример для случайной строки:
    example_word = random_string_func()
    palindrome = Palindrome(example_word)

    example_palindrome_mirror_index = Palindrome.mirror_index(palindrome)
    if example_palindrome_mirror_index == True:
        print(f'Строка {example_word} является палиндромом.')
    else:
        print(f'Строка {example_word} не является палиндромом.')

    # Пример для строки-палиндрома:
    example_palindrome_word = palindrome_string_func()
    palindrome = Palindrome(example_palindrome_word)

    example_palindrome_mirror_index = Palindrome.mirror_index(palindrome)
    if example_palindrome_mirror_index == True:
        print(f'Строка {example_palindrome_word} является палиндромом.')
    else:
        print(f'Строка {example_palindrome_word} не является палиндромом.')
