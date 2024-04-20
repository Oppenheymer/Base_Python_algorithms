# !/usr/bin/env python
# -- coding: utf-8 --
"""
@Filename:   Task3_test_palindrome.py
@Date:       20.04.2024
@Time:       15:21
@Author:     Mentor
@Software:   PyCharm
"""
# Добавляем модуль тестирования функции
import unittest
# Из файла импортируем функцию создания случайной строки
from Task3_palindrome_generator import random_string_func, \
    palindrome_string_func
# Из файла импортируем саму функцию для проверки на палиндром
from Task3_palindrome import Palindrome


class PalindromeTestCase(unittest.TestCase):
    """
    Класс для тестирования функции cycle
    класса Palindrome Task3_palindrome.py
    (Проверка слова на палиндром методом зеркальной индексации массива)

    В тестируемом классе будет взят 2 метод проверки на палиндром
    (функция cycle) - использование цикла и сравнение символов
    на симметричных позициях.
    Исходной последовательностью будет случайное слово, отобранное по 1 методу
    (функция mirror_index) - использование зеркальной индексации массива
    """

    def test_palindrome_func(self):
        """
        Тест-функция проверяет, являются ли строки палиндромом или нет.
        Пример входной строки:
            asa128t45t6t54t821asa
        Выходное значение:
            логическое утверждение (True или False)
        """
        # Задаем слово-палиндром, случайным образом сгенерированное по 1 методу
        test_word = palindrome_string_func()
        # Преобразуем сгенерированное слово к объекту класса Palindrome
        palindrome = Palindrome(test_word)
        # Проверяем сгенерированное слово на палиндром 2 методом
        # Результат - логическое утверждение (True или False)
        is_palindrome = Palindrome.cycle(palindrome)

        # Проверяем истинность значения
        self.assertTrue(is_palindrome)


# Проверка теста
if __name__ == '__main__':
    unittest.main()
